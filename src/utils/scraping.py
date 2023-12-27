"""Main module for scraping functions."""

import logging
import re
from typing import Callable, Dict, List

import numpy as np
import requests
from apscheduler.schedulers.background import BackgroundScheduler
from bs4 import BeautifulSoup

from src.utils.backend import Backend
from src.utils.tools import Server, Website


def schedule_scrapping() -> None:
    """
    Schedule the scrapping of the kamas values
    """
    scheduler = BackgroundScheduler()

    for server in [server.value for server in Server.__members__.values()]:
        scheduler.add_job(
            get_current_kamas_value,
            "interval",
            args=[server],
            minutes=10,
        )
    print("Start the scheduler")
    scheduler.start()


def get_kamas_price_from_kamas_facile_endpoint(server: str) -> float:
    """
    Get the kamas price from kamas facile endpoint

    Args:
        server (str): the server name

    Raises:
        Exception: if the endpoint is not available

    Returns:
        float: the kamas price
    """
    url = f"https://www.kamasfacile.com/fr/{server}"
    response = requests.get(url, timeout=5)

    if response.status_code != 200:
        raise requests.exceptions.RequestException("Endpoint is not available")

    soup = BeautifulSoup(response.text, "html.parser")

    product_prices = soup.find_all("span", class_="product-price")
    re_pattern = r"(\d+,\d{2})\s*€"

    prices: List[float] = []
    for price in product_prices:
        match = re.search(re_pattern, price.text)
        value = float(match[1].replace(",", "."))
        prices.append(value)

    return min(prices)


def get_kamas_from_lekamas(server: str) -> float:
    """
    Get the kamas price from lekamas

    Args:
        server (str): the server name

    Raises:
        ValueError: if the server is not found

    Returns:
        float: the kamas price
    """
    match server:
        case "boune":
            server_info = {
                "option[389]": "1449",
                "option[390]": "1453",
            }
            divide_by = 1
        case "crail":  # /2
            server_info = {
                "option[389]": "1450",
                "option[390]": "1062",
            }
            divide_by = 2
        case "eratz":  # /10
            server_info = {
                "option[389]": "1052",
                "option[390]": "1066",
            }
            divide_by = 10
        case "galgarion":  # /2
            server_info = {
                "option[389]": "1451",
                "option[390]": "1062",
            }
            divide_by = 2
        case "henual":  # /2
            server_info = {
                "option[389]": "1054",
                "option[390]": "1062",
            }
            divide_by = 2
        case _:
            raise ValueError("Server not found")

    url = "https://www.lekamas.fr/index.php?route=journal2/ajax/price"

    data = {"option[388]": "", "quantity": "1", "product_id": "136"}
    payload = data | server_info
    headers = {
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    }
    response = requests.post(url, headers=headers, data=payload, timeout=5)

    value = response.json()["price"].replace("€", "").replace(",", ".")
    value = float(value) / divide_by
    return round(value, 2)


def get_kamas_price_from_mode_marchand(server: str) -> float:
    """
    Get the kamas price from mode marchand

    Args:
        server (str): the server name

    Raises:
        Exception: if the endpoint is not available
        Exception: if the server is not found

    Returns:
        float: the kamas price
    """
    endpoint = "https://www.mode-marchand.net/annonces/dofus-retro/kamas"
    match server:
        case Server.BOUNE.value:
            url = f"{endpoint}?online=1&server%5B%5D=130"
        case Server.CRAIL.value:
            url = f"{endpoint}?online=1&server%5B%5D=128"
        case Server.ERATZ.value:
            url = f"{endpoint}?online=1&server%5B%5D=126"
        case Server.GALGARION.value:
            url = f"{endpoint}?online=1&server%5B%5D=129"
        case _:
            raise ValueError("Server not found")

    response = requests.get(url, timeout=5)

    if response.status_code != 200:
        raise requests.exceptions.RequestException("Endpoint is not available")

    soup = BeautifulSoup(response.text, "html.parser")
    product_prices = soup.find_all("div", class_="card-footer")

    prices: List[float] = []
    regex_pattern = r"\d+\.\d+€(?: - \d+\.\d+€)?"
    for price in product_prices:
        price = price.text
        match = re.search(regex_pattern, price)
        if not match:
            continue
        price = match[0].replace("€", "").replace(" ", "").split("-")[0]
        prices.append(float(price))

    return min(prices)


def get_kamas_from_try_and_judge(server: str) -> float:
    """
    Get the kamas price from try and judge

    Args:
        server (str): the server name

    Raises:
        Exception: if the endpoint is not available
        Exception: if the server is not found

    Returns:
        float: the kamas price
    """
    endpoint = "https://www.tryandjudge.com/fr/retro-kamas"
    match server:
        case Server.BOUNE.value:
            url = f"{endpoint}/boune/1m-kamas-boune"
        case Server.CRAIL.value:
            url = f"{endpoint}/crail/3m-kamas-crail"
        case Server.GALGARION.value:
            url = f"{endpoint}/galgarion/3m-kamas-galgarion"
        case _:
            raise ValueError("Server not found")

    response = requests.get(url, timeout=5)

    if response.status_code != 200:
        raise requests.exceptions.RequestException("Endpoint is not available")

    soup = BeautifulSoup(response.text, "html.parser")
    product_prices = soup.find_all("span", class_="current-price")
    kamas_value = product_prices[0].text

    price = float(kamas_value.replace("€", "").replace(",", "."))
    return price if server == "boune" else round(price / 3, 2)


def get_d_two_gateway_price(server: str) -> float:
    """
    Get the kamas price from D2 gateway

    Args:
        server (str): the server name

    Raises:
        Exception: if the endpoint is not available

    Returns:
        float: the kamas price
    """
    endpoint = "https://fr.d2gate.net/api/offers"
    start_query = "?finalEntityId="
    end_query = (
        "&initialEntityIds=55%2C54%2C6%2C9%2C4%2C3%2C7%2C69%2C47%2C5%2C57%2C8%2C70"
        + "&max=1&min=1&onlyConnected=1&order=price"
    )
    match server:
        case Server.BOUNE.value:
            url = f"{endpoint}{start_query}34{end_query}"
        case Server.CRAIL.value:
            url = f"{endpoint}{start_query}35{end_query}"
        case Server.ERATZ.value:
            url = f"{endpoint}{start_query}36{end_query}"
        case Server.GALGARION.value:
            url = f"{endpoint}{start_query}37{end_query}"
        case Server.HENUAL.value:
            url = f"{endpoint}{start_query}36{end_query}"
        case _:
            raise ValueError("Server not found")
    response = requests.get(url, timeout=5)

    if response.status_code != 200:
        raise requests.exceptions.RequestException("Endpoint is not available")

    response = response.json()

    return float(response["result"][0]["price"])


def get_daily_kamas_value(server: str) -> dict | None:
    """
    Get the daily kamas value

    Args:
        server (str): the server name

    Returns:
        dict | None: the daily kamas value
    """
    backend = Backend()
    try:
        if response := backend.backend_get_daily_kamas_value(server):
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
        "kamas_dict": {"None": 0},
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
        Website.MODE_MARCHAND.value[0]: get_kamas_price_from_mode_marchand,
        Website.TRY_AND_JUDGE.value[0]: get_kamas_from_try_and_judge,
        Website.LE_KAMAS.value[0]: get_kamas_from_lekamas,
    }.items():
        get_kamas_value_from_websites_safully(kamas_dict, name, callback, server)

    kamas_lst = list(kamas_dict.values())
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
