# MIT License
#
# Copyright (c) 2023 Clément RAOUL
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


"""Module for backend requests."""

import os

import requests


class Backend:
    """
    To make requests to the backend
    """

    def __init__(self):
        self.host = os.environ.get("BACKEND_HOST", "localhost")

    def backend_get_two_last_kamas_value(self, server: str) -> dict | None:
        """
        backend endpoint to get the daily kamas value

        Args:
            server (str): the server name

        Raises:
            Exception: if the endpoint is not available

        Returns:
            dict | None: the daily kamas value
        """
        return self._get(":8000/today?server=", server)

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
        return self._get(":8000/yesterday?server=", server)

    def _get(self, query: str, server: str) -> dict | None:
        """
        Get the kamas value from the backend

        Args:
            query (str): query to the backend
            server (str): the server name

        Raises:
            requests.exceptions.RequestException: if the endpoint is not available

        Returns:
            dict | None: the kamas value
        """
        response = requests.get(url=f"http://{self.host}{query}{server}", timeout=5)
        if response.status_code != 200:
            raise requests.exceptions.RequestException("Endpoint is not available")
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
            url=f"http://{self.host}:8000/kamas?server={server}&scope={scope}",
            timeout=5,
        )
        if response.status_code != 200:
            raise requests.exceptions.RequestException("Endpoint is not available")
        return response.json() or None

    # pylint: disable=too-many-arguments
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
        response = requests.post(
            url=f"http://{self.host}:8000/kamas", json=body, timeout=5
        )
        if response.status_code != 200:
            raise requests.exceptions.RequestException("Endpoint is not available")
