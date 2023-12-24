import os

import requests


class Backend:
    def __init__(self):
        self.host = os.environ.get("BACKEND_HOST", "localhost")

    def backend_get_daily_kamas_value(self, server: str) -> dict | None:
        """
        backend endpoint to get the daily kamas value

        Args:
            server (str): the server name

        Raises:
            Exception: if the endpoint is not available

        Returns:
            dict | None: the daily kamas value
        """
        response = requests.get(url=f"http://{self.host}:8000/today?server={server}")
        if response.status_code != 200:
            raise requests.exceptions.RequestException("Endpoint is not available")
        else:
            return response.json() or None

    def backend_get_yesterday_kamas_value(self, server: str) -> dict | None:
        """
        backend endpoint to get the yesterday kamas value

        Args:
            server (str): the server name

        Raises:
            Exception: if the endpoint is not available

        Returns:
            dict | None: the yesterday kamas value
        """
        response = requests.get(
            url=f"http://{self.host}:8000/yesterday?server={server}"
        )
        if response.status_code != 200:
            raise requests.exceptions.RequestException("Endpoint is not available")
        else:
            return response.json() or None

    def backend_get_scope_kamas_value(self, server: str, scope: str) -> dict | None:
        """
        backend endpoint to get all kamas value

        Args:
            server (str): the server name
            scope (str): the scope (day, week, month)

        Raises:
            Exception: if the endpoint is not available

        Returns:
            dict | None: all kamas value
        """
        response = requests.get(
            url=f"http://{self.host}:8000/kamas?server={server}&scope={scope}"
        )
        if response.status_code != 200:
            raise requests.exceptions.RequestException("Endpoint is not available")
        else:
            return response.json() or None

    def backend_post_daily_kamas_value(
        self, values: list, mean: float, max_: float, min_: float, server: str
    ) -> None:
        """
        backend endpoint to post the daily kamas value

        Args:
            values (list): list of kamas value
            mean (float): mean of kamas value
            max_ (float): max of kamas value
            min_ (float): min of kamas value
            server (str): the server name

        Raises:
            Exception: if the endpoint is not available
        """
        body = {
            "kamas_dict": values,
            "average": mean,
            "max": max_,
            "min": min_,
            "server": server,
        }
        response = requests.post(url=f"http://{self.host}:8000/kamas", json=body)
        if response.status_code != 200:
            raise requests.exceptions.RequestException("Endpoint is not available")
