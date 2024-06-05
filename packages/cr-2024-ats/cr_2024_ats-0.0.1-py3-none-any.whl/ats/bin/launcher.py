"""ats.bin.launcher module."""

# imports
from ats.bin.utils import LaunchArguments
from ats.core.models.base.app import BaseApp
from ats.web.app import WebApp


def main(launch_arguments: LaunchArguments) -> None:
    """Start the actual application.

    Args:
        launch_arguments (LaunchArguments): The arguments to start the app
    Returns:
        None
    """
    # Create a new instance of the WebAPP based on the BaseApp class
    app: BaseApp = WebApp(server_ip=launch_arguments.server_ip, server_port=launch_arguments.server_port)

    # Start the app
    app.run()


def cli() -> None:
    """The CLI entrypoint.

    This is the CLI entrypoint when the ats_launcher is used.
    This function parses env arguments and calls the main function with the arguments.

    Args:

    Returns:
        None
    """
    launch_arguments: LaunchArguments = LaunchArguments.get_arguments()
    main(launch_arguments)


# If the launcher is started via the Python interpreter instead of the CLI entrypoint.
if __name__ == "main":
    # Start the CLI function that would normally be called by the entrypoint
    cli()
