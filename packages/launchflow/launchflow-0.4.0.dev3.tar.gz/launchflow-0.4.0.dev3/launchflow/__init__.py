# ruff: noqa
import asyncio
from contextlib import asynccontextmanager, contextmanager

from launchflow.config import config
from launchflow.resource import Resource

from . import aws, docker, fastapi, gcp
from .flows.resource_flows import create, destroy
from .generics import Postgres, Redis

# TODO: Add generic resource imports, like Postgres, StorageBucket, etc.
# This should probably live directly under launchflow, i.e. launchflow/postgres.py


async def connect_all(*resources: Resource):
    connect_tasks = [resource.outputs_async() for resource in resources]
    await asyncio.gather(*connect_tasks)


def is_deployment():
    return config.env.deployment_id is not None


project = config.project
environment = config.environment
