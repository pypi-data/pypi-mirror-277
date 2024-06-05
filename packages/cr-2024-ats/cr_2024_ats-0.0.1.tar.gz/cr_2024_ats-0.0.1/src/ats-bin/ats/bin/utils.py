"""ats.bin.utils module."""

# future imports
from __future__ import annotations

# imports
import argparse
import os
from dataclasses import dataclass, fields


@dataclass
class LaunchArguments:
    """A class for storing parsed launch arguments."""

    server_ip: str
    server_port: int

    @staticmethod
    def __get_env_arguments() -> dict:
        """Retrieve the local environment variables based on the class fields.

        Args:

        Returns:
            dict: A dictionary containing the ENV arguments.
        """
        # Get the arguments from the os based on this dataclass fields
        env_arguments: dict = {
            field.name: os.getenv(field.name) for field in fields(LaunchArguments) if os.getenv(field.name) is not None
        }

        # Return the arguments as dictionary
        return env_arguments

    @staticmethod
    def __get_cli_arguments() -> dict:
        """Retrieve the cli arguments that have been passed to the launcher.

        Args:

        Returns:
            dict: A dictionary containing the CLI arguments.
        """
        argument_parser: argparse.ArgumentParser = argparse.ArgumentParser()
        argument_parser.prog = "ats_launcher"
        argument_parser.version = "1.0.0"  # type: ignore
        argument_parser.epilog = "For more information: https://github.com/CyberRiddles/cr-2024-ats/tree/main"

        argument_parser.add_argument(
            "-s",
            dest="server_ip",
            action="store",
            required=False,
            type=str,
            help="The ip the server is hosted on.",
        )

        argument_parser.add_argument(
            "-p",
            dest="server_port",
            action="store",
            required=False,
            type=int,
            help="The port the server listens on.",
        )

        cli_arguments: dict = vars(argument_parser.parse_args())
        return cli_arguments

    @staticmethod
    def get_arguments() -> LaunchArguments:
        """Get the launch arguments from the ENV, Config and CLI.

        Parse the arguments from the ENV, Config and CLI in that order.
        This means CLI has priority over Config which has priority over CLI.

        Args:

        Returns:
            LaunchArguments: A LaunchArguments instance that contains launch arguments.
        """
        # A dict that will store the arguments that have been retrieved
        arguments: dict = {}

        # Get environment arguments
        env_arguments: dict = LaunchArguments.__get_env_arguments()
        arguments.update(env_arguments)

        # Get config file arguments
        # <Not implemented for this puzzle>

        # Get cli arguments
        cli_arguments: dict = LaunchArguments.__get_cli_arguments()
        arguments.update(cli_arguments)

        # Convert the arguments dict to a LaunchArguments instance.
        launch_arguments: LaunchArguments = LaunchArguments(**arguments)

        # Return the launch arguments
        return launch_arguments
