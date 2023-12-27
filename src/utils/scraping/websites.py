"""Functions to scrap kamas price from differents websites"""

import re
from typing import List

import requests
from bs4 import BeautifulSoup

from src.utils.tools import Server


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
    url = f"https://www.kamasfacile.com/fr/{server}/1m-kamas-{server}"
    response = requests.get(url, timeout=5)

    if response.status_code != 200:
        raise requests.exceptions.RequestException("Endpoint is not available")

    soup = BeautifulSoup(response.text, "html.parser")

    product_price = soup.find("span", class_="current-price-value")
    return float(product_price.text.replace(",", ".").replace("€", ""))


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
        case Server.BOUNE.value:
            server_info = {
                "option[389]": "1449",
                "option[390]": "1453",
            }
            divide_by = 1
        case Server.CRAIL.value:
            server_info = {
                "option[389]": "1450",
                "option[390]": "1062",
            }
            divide_by = 2
        case Server.ERATZ.value:
            server_info = {
                "option[389]": "1052",
                "option[390]": "1066",
            }
            divide_by = 10
        case Server.GALGARION.value:
            server_info = {
                "option[389]": "1451",
                "option[390]": "1062",
            }
            divide_by = 2
        case Server.HENUAL.value:
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
        case Server.HENUAL.value:
            url = f"{endpoint}?online=1&server%5B%5D=127"
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
        case "boune":
            url = f"{endpoint}/boune/1m-kamas-boune"
            divided_by = 1
        case "crail":
            url = f"{endpoint}/crail/3m-kamas-crail"
            divided_by = 3
        case "galgarion":
            url = f"{endpoint}/galgarion/3m-kamas-galgarion"
            divided_by = 3
        case _:
            raise ValueError("Server not found")

    response = requests.get(url, timeout=5)

    if response.status_code != 200:
        raise requests.exceptions.RequestException("Endpoint is not available")

    soup = BeautifulSoup(response.text, "html.parser")
    product_prices = soup.find("span", class_="current-price-value")
    kamas_value = product_prices.text

    price = float(kamas_value.replace("€", "").replace(",", "."))
    return round(price / divided_by, 2)


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


def get_kamas_from_i_game_gold(server: str) -> float:
    """
    Get the price of 1M of kamas from iGameGold

    Args:
        server (str): The server name

    Returns:
        float: The price of 1M of kamas
    """

    match server:
        case Server.BOUNE.value:
            divided_by = 1
        case Server.CRAIL.value:
            divided_by = 5
        case Server.ERATZ.value:
            divided_by = 20
        case Server.GALGARION.value:
            divided_by = 5
        case Server.HENUAL.value:
            divided_by = 6
        case _:
            raise ValueError("Server not found")

    url = "https://www.igamegold.com/fr/Dofus-Kamas?gad_source=1"

    response = requests.get(url, timeout=5)
    soup = BeautifulSoup(response.text, "html.parser")
    calculate_price_elements = soup.find_all(class_="calculate-price")

    for element in calculate_price_elements:
        if element.find("div", class_="title", string=f"{server.capitalize()} - 1.3"):
            if price_span := element.find("span", class_="price-value"):
                return round(float(price_span.text) / divided_by, 2)
