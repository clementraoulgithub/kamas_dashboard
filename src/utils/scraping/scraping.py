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


"""Main module for scraping functions."""

import logging
from typing import Callable, Dict

import numpy as np
import requests
from apscheduler.schedulers.background import BackgroundScheduler

from src.utils.backend import Backend
from src.utils.enums import ServerClassic, ServerRetro, ServerTouch, Website
from src.utils.scraping.websites import (
    get_d_two_gateway_price,
    get_kamas_from_i_game_gold,
    get_kamas_from_lekamas,
    get_kamas_from_try_and_judge,
    get_kamas_price_from_kamas_facile_endpoint,
)


def schedule_scrapping() -> None:
    """
    Schedule the scrapping of the kamas values
    """
    scheduler = BackgroundScheduler()

    for server in [server.value for server in ServerRetro.__members__.values()]:
        scheduler.add_job(
            get_current_kamas_value,
            "interval",
            args=[server],
            minutes=29,
        )

    for server in [server.value for server in ServerClassic.__members__.values()]:
        scheduler.add_job(
            get_current_kamas_value,
            "interval",
            args=[server],
            minutes=31,
        )

    for server in [server.value for server in ServerTouch.__members__.values()]:
        scheduler.add_job(
            get_current_kamas_value,
            "interval",
            args=[server],
            minutes=33,
        )

    print("Start the scheduler")
    scheduler.start()


def get_two_last_kamas_value(server: str) -> dict | None:
    """
    Get the daily kamas value

    Args:
        server (str): the server name

    Returns:
        dict | None: the daily kamas value
    """
    backend = Backend()
    try:
        if response := backend.backend_get_two_last_kamas_value(server):
            return response
    except requests.exceptions.RequestException as e:
        logging.error("Error while getting daily kamas value: %s", e)
    return None


def get_yesterday_kamas_value(server: str) -> dict | None:
    """
    Get the yesterday kamas value

    Args:
        server (str): the server name

    Returns:
        dict | None: the yesterday kamas value
    """
    backend = Backend()
    try:
        if response := backend.backend_get_yesterday_kamas_value(server):
            return response
    except requests.exceptions.RequestException as e:
        logging.error("Error while getting yesterday kamas value: %s", e)

    return {
        "timestamp": "1970-01-01T00:00:00.0+00:00",
        "average": 0,
        "max": 0,
        "min": 0,
        "kamas_dict": {"": 0},
        "server": server,
    }


def get_scope_kamas_value(server: str, scope: str) -> dict | None:
    """
    Get all kamas value

    Args:
        server (str): the server name

    Returns:
        dict | None: all kamas value
    """
    backend = Backend()
    try:
        if response := backend.backend_get_scope_kamas_value(server, scope):
            return response
    except requests.exceptions.RequestException as e:
        logging.error("Error while getting yesterday kamas value: %s", e)

    return [
        {
            "timestamp": "1970-01-01T00:00:00.0+00:00",
            "average": 0,
            "max": 0,
            "min": 0,
            "kamas_dict": {"None": 0},
            "server": server,
        }
    ]


def get_current_kamas_value(server: str) -> None:
    """
    Get the current kamas value

    Args:
        server (str): the server name
    """
    backend = Backend()
    kamas_dict: Dict[str, float] = {}

    for name, callback in {
        Website.D2GATE.value[0]: get_d_two_gateway_price,
        Website.KAMAS_FACILE.value[0]: get_kamas_price_from_kamas_facile_endpoint,
        Website.TRY_AND_JUDGE.value[0]: get_kamas_from_try_and_judge,
        Website.LE_KAMAS.value[0]: get_kamas_from_lekamas,
        Website.I_GAME_GOLD.value[0]: get_kamas_from_i_game_gold,
    }.items():
        get_kamas_value_from_websites_safully(kamas_dict, name, callback, server)

    if kamas_lst := list(kamas_dict.values()):
        kamas_lst = [kamas for kamas in kamas_lst if kamas is not None]
        mean = round(np.mean(kamas_lst), 2)
        max_ = max(kamas_lst)
        min_ = min(kamas_lst)

    if mean and max_ and min_:
        try:
            backend.backend_post_daily_kamas_value(kamas_dict, mean, max_, min_, server)
        except requests.exceptions.RequestException as e:
            logging.error("Error while posting daily kamas value: %s", e)


# pylint: disable=broad-exception-caught
def get_kamas_value_from_websites_safully(
    kamas_dict: dict, name: str, callback: Callable, server: str
) -> None:
    """
    Get the kamas value from websites safully with exception handling

    Args:
        kamas_dict (dict): the kamas dict
        name (str): the website name
        callback (Callable): the callback function
        server (str): the server name
    """
    try:
        kamas_dict[name] = callback(server)
    except requests.exceptions.RequestException as e:
        logging.warning("Endpoint error from %s for server %s: %s", name, server, e)
    except Exception as e:
        logging.error(
            "Error while getting kamas value from %s for server %s: %s", name, server, e
        )
