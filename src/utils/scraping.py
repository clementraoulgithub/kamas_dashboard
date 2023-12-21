import datetime
import logging
import re
from typing import Callable, Dict, List

import numpy as np
import requests
from bs4 import BeautifulSoup

from src.utils.backend.backend import (
    backend_get_daily_kamas_value, backend_get_kamas_value,
    backend_get_yesterday_kamas_value,
    backend_post_daily_kamas_value
)


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
    response = requests.get(url)

    if response.status_code != 200:
        requests.exceptions.RequestException("Endpoint is not available")

    soup = BeautifulSoup(response.text, "html.parser")

    product_prices = soup.find_all("span", class_="product-price")
    re_pattern = r"(\d+,\d{2})\s*€"

    prices: List[float] = []
    for price in product_prices:
        match = re.search(re_pattern, price.text)
        value = float(match[1].replace(",", "."))
        prices.append(value)

    return min(prices)


def get_kamas_price_from_fun_shop(server: str) -> float:
    """
    Get the kamas price from fun shop

    Args:
        server (str): the server name

    Raises:
        Exception: if the endpoint is not available
        Exception: if the server is not found

    Returns:
        float: the kamas price
    """
    url = "https://www.funshopes.com/purchaseServers.php?lang=fr&g=17"
    response = requests.get(url)

    if response.status_code != 200:
        raise requests.exceptions.RequestException("Endpoint is not available")

    soup = BeautifulSoup(response.text, "html.parser")
    product_prices = soup.find_all("span", class_="prc")

    match server:
        case "boune":
            index = 0
        case "crail":
            index = 1
        case "galgarion":
            index = 3
        case _:
            raise ValueError("Server not found")

    kamas_value = product_prices[index].text
    kamas_value = kamas_value.split("\\")[0]

    return float(kamas_value)


def get_kamas_price_from_ig_play(server: str) -> float:
    """
    Get the kamas price from ig play

    Args:
        server (str): the server name

    Raises:
        Exception: if the endpoint is not available
        Exception: if the server is not found

    Returns:
        float: the kamas price
    """
    url = "https://www.igplays.com/selltous.php?gclid=Cj0KCQiAm4WsBhCiARIsAEJIEzUwqjGYNyAMFJou72q-kjGsSxZb1Gsd5JML8AJ09kimevCf7JWUQ0gaApsWEALw_wcB"
    response = requests.get(url)

    if response.status_code != 200:
        raise requests.exceptions.RequestException("Endpoint is not available")

    soup = BeautifulSoup(response.text, "html.parser")
    product_prices = soup.find_all("span", class_="prc")

    match server:
        case "boune":
            index = 0
        case "crail":
            index = 1
        case "galgarion":
            index = 3
        case _:
            raise ValueError("Server not found")

    kamas_value = product_prices[index].text
    kamas_value = kamas_value.split("\\")[0]

    return float(kamas_value)


def get_kamas_price_from_leskamas(server: str) -> float:
    """
    Get the kamas price from leskamas

    Args:
        server (str): the server name

    Raises:
        Exception: if the endpoint is not available

    Returns:
        float: the kamas price
    """
    url = "https://www.leskamas.com/vendre-des-kamas.html"
    response = requests.get(url)

    if response.status_code != 200:
        raise requests.exceptions.RequestException("Endpoint is not available")

    soup = BeautifulSoup(response.text, "html.parser")
    server = server.capitalize()
    re_pattern = rf"<td>{server}<\/td>\s*<td>(.*?)<\/td>"
    match = re.search(re_pattern, str(soup))
    return float(match[1].replace("€/M", ""))


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
    match server:
        case "boune":
            url = "https://www.mode-marchand.net/annonces/dofus-retro/kamas?server%5B%5D=130"
        case "crail":
            url = "https://www.mode-marchand.net/annonces/dofus-retro/kamas?server%5B%5D=128"
        case "eratz":
            url = "https://www.mode-marchand.net/annonces/dofus-retro/kamas?server%5B%5D=126"
        case "galgarion":
            url = "https://www.mode-marchand.net/annonces/dofus-retro/kamas?server%5B%5D=129"
        case _:
            raise ValueError("Server not found")

    response = requests.get(url)

    if response.status_code != 200:
        raise requests.exceptions.RequestException("Endpoint is not available")

    soup = BeautifulSoup(response.text, "html.parser")
    product_prices = soup.find_all("div", class_="card-footer")

    prices: List[float] = []
    for price in product_prices:
        price = price.text
        regex_pattern = r"\d+\.\d+€(?: - \d+\.\d+€)?"
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
    match server:
        case "boune":
            url = "https://www.tryandjudge.com/fr/retro-kamas/boune/1m-kamas-boune"
        case "crail":
            url = "https://www.tryandjudge.com/fr/retro-kamas/crail/3m-kamas-crail"
        case "galgarion":
            url = "https://www.tryandjudge.com/fr/retro-kamas/galgarion/3m-kamas-galgarion"
        case _:
            raise ValueError("Server not found")

    response = requests.get(url)

    if response.status_code != 200:
        raise requests.exceptions.RequestException("Endpoint is not available")

    soup = BeautifulSoup(response.text, "html.parser")
    product_prices = soup.find_all("span", class_="current-price")
    kamas_value = product_prices[0].text

    price = float(kamas_value.replace("€", "").replace(",", "."))
    return price if server == "boune" else round(price / 3, 2)


def get_daily_kamas_value(server: str) -> dict | None:
    """
    Get the daily kamas value

    Args:
        server (str): the server name

    Returns:
        dict | None: the daily kamas value
    """
    if response := backend_get_daily_kamas_value(server):
        return response
    else:
        return {"timestamp": "1970-01-01T00:00:00.0+00:00", "average": 0, "max": 0, "min": 0, "kamas_dict": {"None": 0}, "server": server}


def get_yesterday_kamas_value(server: str) -> dict | None:
    """
    Get the yesterday kamas value

    Args:
        server (str): the server name

    Returns:
        dict | None: the yesterday kamas value
    """
    if response := backend_get_yesterday_kamas_value(server):
        return response
    else:
        return {"timestamp": "1970-01-01T00:00:00.0+00:00", "average": 0, "max": 0, "min": 0, "kamas_dict": {"None": 0}, "server": server}
    
def get_all_kamas_value(server: str) -> dict | None:
    """
    Get all kamas value

    Args:
        server (str): the server name

    Returns:
        dict | None: all kamas value
    """
    if response := backend_get_kamas_value(server):
        return response
    else:
        return [{"timestamp": "1970-01-01T00:00:00.0+00:00", "average": 0, "max": 0, "min": 0, "kamas_dict": {"None": 0}, "server": server}]


def get_current_kamas_value(server: str) -> None:
    """
    Get the current kamas value

    Args:
        server (str): the server name
    """
    logging.info(f"Getting kamas value for server {server}")
    kamas_dict: Dict[str, float] = {}
    for name, callback in {
        "Kamas facile": get_kamas_price_from_kamas_facile_endpoint,
        "Fun shop": get_kamas_price_from_fun_shop,
        "Les kamas": get_kamas_price_from_leskamas,
        "Mode marchand": get_kamas_price_from_mode_marchand,
        "Try and judge": get_kamas_from_try_and_judge,
        "Ig plays": get_kamas_price_from_ig_play,
    }.items():
        get_kamas_value_from_websites_safully(kamas_dict, name, callback, server)

    kamas_lst = list(kamas_dict.values())
    mean = round(np.mean(kamas_lst), 2)
    max_ = max(kamas_lst)
    min_ = min(kamas_lst)

    if mean and max_ and min_:
        backend_post_daily_kamas_value(kamas_dict, mean, max_, min_, server)


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
    except ValueError:
        pass
    except requests.exceptions.RequestException as e:
        logging.warning(
            f"Error while getting kamas value from {name} for server {server}: {e}"
        )
