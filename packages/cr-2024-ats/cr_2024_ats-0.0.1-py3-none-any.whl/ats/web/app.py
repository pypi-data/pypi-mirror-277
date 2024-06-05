"""ats.web.app module."""

# Imports
from ats.core.models.base.app import BaseApp
from ats.web.pages.default import DefaultPageGenerator
from flask import Flask
from gevent.pywsgi import WSGIServer


class WebApp(BaseApp):
    """A BaseAPP implementation for hosting the web app."""

    __server_ip: str
    __server_port: int

    def __init__(self, server_ip: str = "127.0.0.1", server_port: int = 5000):
        """Initialize an WebAPP instance.

        Args:
            server_ip (str): The ip the server is hosted on.
            server_port (int): The port the server listens on.

        Returns:
            None
        """
        # Assign the function variables to the class instance
        self.__server_ip = server_ip
        self.__server_port = server_port

        # Check the variables that have been passed
        self.check_parameters()

    def check_parameters(self) -> None:
        """Check the APP run parameters.

        Check the parameters that have been passed to the app.

        Args:

        Returns:
            None
        """
        if not self.__server_ip or self.__server_ip == "":
            raise ValueError("Incorrect server ip")

        if not self.__server_port or self.__server_port <= 0:
            raise ValueError("Incorrect server port")

    def run(self) -> None:
        """Start the app instance.

        Args:

        Returns:
            None
        """
        # Create a new flask app instance
        flask_app: Flask = Flask(__name__)

        # Register the default flask route
        flask_app.add_url_rule(
            rule="/",
            endpoint="default",
            view_func=DefaultPageGenerator.generate_default_page,
        )

        # Start the flask app instance via a gevent WSGIServer
        http_server: WSGIServer = WSGIServer(listener=(self.__server_ip, self.__server_port), application=flask_app)
        http_server.serve_forever()
