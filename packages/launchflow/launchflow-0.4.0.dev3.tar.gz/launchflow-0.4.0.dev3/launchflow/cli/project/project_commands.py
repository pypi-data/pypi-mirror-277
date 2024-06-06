import beaupy
import httpx
import rich
import typer

from launchflow import exceptions
from launchflow.cli.utils import print_response
from launchflow.cli.utyper import UTyper
from launchflow.clients import async_launchflow_client_ctx
from launchflow.clients.projects_client import ProjectsAsyncClient
from launchflow.config import config
from launchflow.config.launchflow_yaml import LaunchFlowBackend
from launchflow.exceptions import LaunchFlowException
from launchflow.flows.project_flows import create_project

app = UTyper(help="Interact with your LaunchFlow projects.")


@app.command()
async def list():
    """Lists all current projects in your account."""

    if config.launchflow_yaml is not None and isinstance(
        config.launchflow_yaml.backend, LaunchFlowBackend
    ):
        base_url = config.launchflow_yaml.backend.launchflow_url
    else:
        base_url = config.settings.launch_service_address
    async with httpx.AsyncClient(timeout=60) as client:
        proj_client = ProjectsAsyncClient(http_client=client, base_url=base_url)
        projects = await proj_client.list(config.settings.default_account_id)
    print_response(
        "Projects",
        {
            "projects": [
                projects.model_dump(exclude_defaults=True) for projects in projects
            ]
        },
    )


@app.command()
async def create(
    account_id: str = typer.Option(
        None,
        help="The account ID to fetch. Of the format `acount_123`. Defaults to the account in your config file.",  # noqa: E501
    ),
    auto_approve: bool = typer.Option(
        False, "--auto-approve", "-y", help="Auto approve project creation."
    ),
):
    """Create a new project in your account."""
    if config.launchflow_yaml is None:
        raise exceptions.LaunchFlowYamlNotFound()
    if not isinstance(config.launchflow_yaml.backend, LaunchFlowBackend):
        typer.echo(
            "launchflow.yaml was not pointed to a LaunchFlow backend. Please update and try again."
        )
        raise typer.Exit(1)
    async with async_launchflow_client_ctx(
        base_url=config.launchflow_yaml.backend.launchflow_url,
        api_key=config.launchflow_yaml.backend.launchflow_api_key,
    ) as client:
        try:
            project = await create_project(
                client=client,
                project_name=config.project,
                account_id=account_id,
                prompt=not auto_approve,
            )
        except LaunchFlowException:
            raise typer.Exit(1)

    if project is not None:
        print_response("Project", project.model_dump(exclude_defaults=True))


@app.command()
async def delete(
    name: str = typer.Argument(..., help="The project name."),
    auto_approve: bool = typer.Option(
        False, "--auto-approve", "-y", help="Auto approve project deletion."
    ),
):
    """Delete a project."""
    if not auto_approve:
        user_confirmation = beaupy.confirm(
            f"Would you like to delete the project `{name}`?",
            default_is_yes=True,
        )
        if not user_confirmation:
            rich.print("[red]✗[/red] Project deletion cancelled.")
            typer.Exit(1)

    if config.launchflow_yaml is not None and isinstance(
        config.launchflow_yaml.backend, LaunchFlowBackend
    ):
        base_url = config.launchflow_yaml.backend.launchflow_url
    else:
        base_url = config.settings.launch_service_address
    try:
        async with async_launchflow_client_ctx(base_url=base_url) as client:
            await client.projects.delete(name)

    except Exception as e:
        typer.echo(e)
        raise typer.Exit(1)

    rich.print("[green]✓[/green] Project deleted.")
