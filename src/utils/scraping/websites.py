"""Functions to scrap kamas price from differents websites"""

import re
from typing import List

import requests
from bs4 import BeautifulSoup

from src.utils.tools import ServerClassic, ServerRetro


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
    if server == ServerClassic.OMBRE.value:
        url = f"https://www.kamasfacile.com/fr/{server}-kamas/3m-kamas-{server}shadow"
    else:
        url = f"https://www.kamasfacile.com/fr/{server}/3m-kamas-{server}"
    response = requests.get(url, timeout=5)

    if response.status_code != 200:
        raise requests.exceptions.RequestException("Endpoint is not available")

    soup = BeautifulSoup(response.text, "html.parser")

    product_price = soup.find("span", class_="current-price-value")
    product_price = float(product_price.text.replace(",", ".").replace("€", ""))
    return round(product_price / 3, 2)


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

    def _setup_payload(arg0: str, server_info, arg2: str, divided_by: int) -> int:
        server_info["option[389]"] = arg0
        server_info["option[390]"] = arg2
        return divided_by

    server_info = {
        "option[389]": "",
        "option[390]": "",
    }
    match server:
        case ServerRetro.BOUNE.value:
            divided_by = _setup_payload("1449", server_info, "1453", 1)
        case ServerRetro.CRAIL.value:
            divided_by = _setup_payload("1450", server_info, "1062", 2)
        case ServerRetro.ERATZ.value:
            divided_by = _setup_payload("1052", server_info, "1066", 10)
        case ServerRetro.GALGARION.value:
            divided_by = _setup_payload("1451", server_info, "1062", 2)
        case ServerRetro.HENUAL.value:
            divided_by = _setup_payload("1054", server_info, "1062", 2)
        case ServerClassic.DRACONIROS.value:
            divided_by = _setup_payload("1055", server_info, "1062", 2)
        case ServerClassic.HELLMINA.value:
            divided_by = _setup_payload("1053", server_info, "1063", 3)
        case ServerClassic.IMAGIRO.value:
            divided_by = _setup_payload("1047", server_info, "1063", 3)
        case ServerClassic.OMBRE.value:
            divided_by = _setup_payload("1445", server_info, "1063", 3)
        case ServerClassic.ORUKAM.value:
            divided_by = _setup_payload("1057", server_info, "1063", 3)
        case ServerClassic.TALKASHA.value:
            divided_by = _setup_payload("1455", server_info, "1063", 3)
        case ServerClassic.TYLEZIA.value:
            divided_by = _setup_payload("1448", server_info, "1063", 3)
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
    value = float(value) / divided_by
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
    endpoint_retro = "https://www.mode-marchand.net/annonces/dofus-retro/kamas"
    endpoint_classique = "https://www.mode-marchand.net/annonces/dofus/kamas"
    query = "?online=1&server%5B%5D="
    match server:
        case ServerRetro.BOUNE.value:
            url = f"{endpoint_retro}{query}130"
        case ServerRetro.CRAIL.value:
            url = f"{endpoint_retro}{query}128"
        case ServerRetro.ERATZ.value:
            url = f"{endpoint_retro}{query}126"
        case ServerRetro.GALGARION.value:
            url = f"{endpoint_retro}{query}129"
        case ServerRetro.HENUAL.value:
            url = f"{endpoint_retro}{query}127"
        case ServerClassic.DRACONIROS.value:
            url = f"{endpoint_classique}{query}122"
        case ServerClassic.HELLMINA.value:
            url = f"{endpoint_classique}{query}121"
        case ServerClassic.IMAGIRO.value:
            url = f"{endpoint_classique}{query}119"
        case ServerClassic.OMBRE.value:
            url = f"{endpoint_classique}{query}123"
        case ServerClassic.ORUKAM.value:
            url = f"{endpoint_classique}{query}120"
        case ServerClassic.TALKASHA.value:
            url = f"{endpoint_classique}{query}125"
        case ServerClassic.TYLEZIA.value:
            url = f"{endpoint_classique}{query}124"
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
    endpoint_retro = "https://www.tryandjudge.com/fr/retro-kamas"
    endpoint_classique = "https://www.tryandjudge.com/fr/dofus-kamas"
    match server:
        case ServerRetro.BOUNE.value:
            url = f"{endpoint_retro}/{server}/1m-kamas-{server}"
            divided_by = 1
        case ServerRetro.CRAIL.value:
            url = f"{endpoint_retro}/{server}/3m-kamas-{server}"
            divided_by = 3
        case ServerRetro.GALGARION.value:
            url = f"{endpoint_retro}/{server}/3m-kamas-{server}"
            divided_by = 3
        case ServerClassic.DRACONIROS.value:
            url = f"{endpoint_classique}/{server}/1m-kamas-{server}"
            divided_by = 1
        case ServerClassic.HELLMINA.value:
            url = f"{endpoint_classique}/{server}/3m-kamas-{server}"
            divided_by = 3
        case ServerClassic.IMAGIRO.value:
            url = f"{endpoint_classique}/{server}/3m-kamas-{server}"
            divided_by = 3
        case ServerClassic.OMBRE.value:
            url = f"{endpoint_classique}/{server}shadow/3m-kamas-{server}"
            divided_by = 3
        case ServerClassic.ORUKAM.value:
            url = f"{endpoint_classique}/{server}/3m-kamas-{server}"
            divided_by = 3
        case ServerClassic.TALKASHA.value:
            url = f"{endpoint_classique}/{server}/3m-kamas-{server}"
            divided_by = 3
        case ServerClassic.TYLEZIA.value:
            url = f"{endpoint_classique}/{server}/3m-kamas-{server}"
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
        case ServerRetro.BOUNE.value:
            url = f"{endpoint}{start_query}34{end_query}"
        case ServerRetro.CRAIL.value:
            url = f"{endpoint}{start_query}35{end_query}"
        case ServerRetro.ERATZ.value:
            url = f"{endpoint}{start_query}36{end_query}"
        case ServerRetro.GALGARION.value:
            url = f"{endpoint}{start_query}37{end_query}"
        case ServerRetro.HENUAL.value:
            url = f"{endpoint}{start_query}36{end_query}"
        case ServerClassic.DRACONIROS.value:
            url = f"{endpoint}{start_query}73{end_query}"
        case ServerClassic.HELLMINA.value:
            url = f"{endpoint}{start_query}74{end_query}"
        case ServerClassic.IMAGIRO.value:
            url = f"{endpoint}{start_query}71{end_query}"
        case ServerClassic.OMBRE.value:
            url = f"{endpoint}{start_query}26{end_query}"
        case ServerClassic.ORUKAM.value:
            url = f"{endpoint}{start_query}72{end_query}"
        case ServerClassic.TALKASHA.value:
            url = f"{endpoint}{start_query}68{end_query}"
        case ServerClassic.TYLEZIA.value:
            url = f"{endpoint}{start_query}75{end_query}"
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
        case ServerRetro.BOUNE.value:
            divided_by = 1
            string = f"{server.capitalize()} - 1.3"
        case ServerRetro.CRAIL.value:
            divided_by = 5
            string = f"{server.capitalize()} - 1.3"
        case ServerRetro.ERATZ.value:
            divided_by = 20
            string = f"{server.capitalize()} - 1.3"
        case ServerRetro.GALGARION.value:
            divided_by = 5
            string = f"{server.capitalize()} - 1.3"
        case ServerRetro.HENUAL.value:
            divided_by = 6
            string = f"{server.capitalize()} - 1.3"
        case ServerClassic.DRACONIROS.value:
            divided_by = 4
            string = f"{server.capitalize()} - Mono"
        case ServerClassic.HELLMINA.value:
            divided_by = 5
            string = "HellMina - Classic"
        case ServerClassic.IMAGIRO.value:
            divided_by = 5
            string = f"{server.capitalize()} - Classic"
        case ServerClassic.OMBRE.value:
            divided_by = 5
            string = f"{server.capitalize()}(Shadow) - Heroic"
        case ServerClassic.ORUKAM.value:
            divided_by = 5
            string = f"{server.capitalize()} - Classic"
        case ServerClassic.TALKASHA.value:
            divided_by = 5
            string = f"{server.capitalize()} - Classic"
        case ServerClassic.TYLEZIA.value:
            divided_by = 5
            string = f"{server.capitalize()} - Classic"
        case _:
            raise ValueError("Server not found")

    url = "https://www.igamegold.com/fr/Dofus-Kamas"

    response = requests.get(url, timeout=5)
    soup = BeautifulSoup(response.text, "html.parser")
    calculate_price_elements = soup.find_all(class_="calculate-price")

    for element in calculate_price_elements:
        if element.find("div", class_="title", string=string):
            if price_span := element.find("span", class_="price-value"):
                return round(float(price_span.text) / divided_by, 2)
