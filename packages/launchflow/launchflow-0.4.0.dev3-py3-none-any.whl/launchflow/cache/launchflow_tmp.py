import logging
import os
import shutil
from dataclasses import dataclass, field
from typing import Dict, Optional

import toml

from launchflow.config import config


def _build_key(project: str, environment: str, product: str, resource: str) -> str:
    return f"{project}:{environment}:{product}:{resource}"


@dataclass
class LaunchFlowCache:
    permanent_cache_file_path: str
    run_cache_file_path: Optional[str]

    # Permanent cache values below
    resource_connection_bucket_paths: Dict[str, str] = field(default_factory=dict)
    gcp_service_account_emails: Dict[str, str] = field(default_factory=dict)

    # Run cache values below
    resource_connection_info: Dict[str, Dict[str, str]] = field(default_factory=dict)

    def get_resource_outputs_bucket_path(
        self, project: str, environment: str, product: str, resource: str
    ) -> Optional[str]:
        key = _build_key(project, environment, product, resource)
        return self.resource_connection_bucket_paths.get(key)

    def set_resource_connection_bucket_path(
        self,
        project: str,
        environment: str,
        product: str,
        resource: str,
        connection_bucket_path: str,
    ):
        key = _build_key(project, environment, product, resource)
        self.resource_connection_bucket_paths[key] = connection_bucket_path
        self.save_permanent_cache_to_disk()

    def delete_resource_connection_bucket_path(
        self, project: str, environment: str, product: str, resource: str
    ):
        key = _build_key(project, environment, product, resource)
        self.resource_connection_bucket_paths.pop(key, None)
        self.save_permanent_cache_to_disk()

    def get_resource_outputs(
        self, project: str, environment: str, product: str, resource: str
    ) -> Optional[Dict[str, str]]:
        key = _build_key(project, environment, product, resource)
        return self.resource_connection_info.get(key)

    def set_resource_outputs(
        self,
        project: str,
        environment: str,
        product: str,
        resource: str,
        connection_info: Dict[str, str],
    ):
        key = _build_key(project, environment, product, resource)
        self.resource_connection_info[key] = connection_info
        self.save_run_cache_to_disk()

    def delete_resource_connection_info(
        self, project: str, environment: str, product: str, resource: str
    ):
        key = _build_key(project, environment, product, resource)
        self.resource_connection_info.pop(key, None)
        self.save_permanent_cache_to_disk()

    def get_gcp_service_account_email(
        self, project: str, environment: str
    ) -> Optional[str]:
        key = f"{project}:{environment}"
        return self.gcp_service_account_emails.get(key)

    def set_gcp_service_account_email(self, project: str, environment: str, email: str):
        key = f"{project}:{environment}"
        self.gcp_service_account_emails[key] = email
        self.save_permanent_cache_to_disk()

    def delete_gcp_service_account_email(self, project: str, environment: str):
        key = f"{project}:{environment}"
        self.gcp_service_account_emails.pop(key, None)
        self.save_permanent_cache_to_disk()

    @classmethod
    def load_from_file(
        cls, permanent_cache_file_path: str, run_cache_file_path: Optional[str]
    ):
        if not os.path.exists(permanent_cache_file_path):
            logging.debug(
                f"The file '{permanent_cache_file_path}' does not exist. Creating with default values."
            )
            return cls(
                permanent_cache_file_path=permanent_cache_file_path,
                run_cache_file_path=run_cache_file_path,
            )

        # Load the permanent cache
        with open(permanent_cache_file_path, "r") as file:
            logging.debug(f"Loading permanent cache from {permanent_cache_file_path}")
            data = toml.load(file)
            resource_connection_bucket_paths = data.get(
                "resource_connection_bucket_paths", {}
            )
            gcp_service_account_emails = data.get("gcp_service_account_emails", {})

        # Load the run cache if it exists
        resource_connection_info = {}
        if run_cache_file_path is not None and os.path.exists(run_cache_file_path):
            logging.debug(f"Loading run cache from {run_cache_file_path}")
            with open(run_cache_file_path, "r") as file:
                run_cache = toml.load(file)
                resource_connection_info = run_cache.get("resource_connection_info", {})

        return cls(
            permanent_cache_file_path=permanent_cache_file_path,
            run_cache_file_path=run_cache_file_path,
            resource_connection_bucket_paths=resource_connection_bucket_paths,
            resource_connection_info=resource_connection_info,
            gcp_service_account_emails=gcp_service_account_emails,
        )

    def save_permanent_cache_to_disk(self):
        data = {
            "resource_connection_bucket_paths": self.resource_connection_bucket_paths,
            "gcp_service_account_emails": self.gcp_service_account_emails,
        }
        os.makedirs(os.path.dirname(self.permanent_cache_file_path), exist_ok=True)
        with open(self.permanent_cache_file_path, "w") as file:
            toml.dump(data, file)
        logging.debug(f"Saved to {self.permanent_cache_file_path}")

    def save_run_cache_to_disk(self):
        if self.run_cache_file_path is None:
            return
        data = {
            "resource_connection_info": self.resource_connection_info,
        }
        os.makedirs(os.path.dirname(self.run_cache_file_path), exist_ok=True)
        with open(self.run_cache_file_path, "w") as file:
            toml.dump(data, file)
        logging.debug(f"Saved to {self.run_cache_file_path}")


def build_cache_file_paths():
    # We use /var/tmp over /tmp since it persists across system reboot
    permanent_tmp_dir = "/var/tmp" if os.name != "nt" else os.environ.get("TEMP")
    temporary_tmp_dir = "/tmp" if os.name != "nt" else os.environ.get("TMP")

    # Build the permanent cache file path
    permanent_cache_file_path = os.path.join(permanent_tmp_dir, "lf", "cache.toml")

    # Build the temporary cache file path
    run_cache_file_path = None
    if config.env.run_id is not None:
        run_cache_file_path = os.path.join(
            temporary_tmp_dir, "lf", config.env.run_id, "cache.toml"
        )
    return permanent_cache_file_path, run_cache_file_path


launchflow_cache = None


def load_launchflow_cache():
    global launchflow_cache
    if launchflow_cache is None:
        permanent_cache_file_path, run_cache_file_path = build_cache_file_paths()
        launchflow_cache = LaunchFlowCache.load_from_file(
            permanent_cache_file_path, run_cache_file_path
        )
    return launchflow_cache


def delete_run_cache_from_disk(run_id: str):
    temporary_tmp_dir = "/tmp" if os.name != "nt" else os.environ.get("TMP")
    run_cache_dir = os.path.join(temporary_tmp_dir, "lf", run_id)
    if not os.path.exists(run_cache_dir):
        logging.debug(f"Run cache directory {run_cache_dir} does not exist.")
        return
    shutil.rmtree(run_cache_dir)
    logging.debug(f"Deleted run cache directory {run_cache_dir}.")
