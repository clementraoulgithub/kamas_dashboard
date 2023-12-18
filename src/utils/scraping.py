import re
from typing import Callable, Dict, List

import numpy as np
import requests
from bs4 import BeautifulSoup

from src.utils.backend.backend import (backend_get_daily_kamas_value,
                                       backend_get_yesterday_kamas_value,
                                       backend_post_daily_kamas_value)


def get_kamas_price_from_kamas_facile_endpoint(server: str):
    url = f"https://www.kamasfacile.com/fr/{server}"
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception("Endpoint is not available")

    soup = BeautifulSoup(response.text, "html.parser")

    product_prices = soup.find_all("span", class_="product-price")
    re_pattern = r"(\d+,\d{2})\s*€"

    prices: List[float] = []
    for price in product_prices:
        match = re.search(re_pattern, price.text)
        value = float(match[1].replace(",", "."))
        prices.append(value)

    return min(prices)


def get_kamas_price_from_fun_shop(server: str):
    url = "https://www.funshopes.com/purchaseServers.php?lang=fr&g=17"
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception("Endpoint is not available")

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
            raise Exception("Server not found")
    
    kamas_value = product_prices[index].text
    kamas_value = kamas_value.split("\\")[0]

    return float(kamas_value)


def get_kamas_price_from_leskamas(server: str):
    url = "https://www.leskamas.com/vendre-des-kamas.html"
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception("Endpoint is not available")

    soup = BeautifulSoup(response.text, "html.parser")
    server = server.capitalize()
    re_pattern = fr"<td>{server}<\/td>\s*<td>(.*?)<\/td>"
    match = re.search(re_pattern, str(soup))
    return float(match[1].replace("€/M", ""))


def get_kamas_price_from_mode_marchand(server: str):
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
            raise Exception("Server not found")
    
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception("Endpoint is not available")

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


def get_daily_kamas_value(server: str):
    if response := backend_get_daily_kamas_value(server):
        return response


def get_yesterday_kamas_value(server: str):
    if response := backend_get_yesterday_kamas_value(server):
        return response


def get_current_kamas_value(server: str) -> None:
    kamas_dict: Dict[str, float] = {}
    for name, callback in {
        "Kamas facile": get_kamas_price_from_kamas_facile_endpoint,
        "Fun shop": get_kamas_price_from_fun_shop,
        "Les kamas": get_kamas_price_from_leskamas,
        "Mode marchand": get_kamas_price_from_mode_marchand,
    }.items():
        get_kamas_value_from_websites_safully(kamas_dict, name, callback, server)

    kamas_lst = list(kamas_dict.values())
    mean = round(np.mean(kamas_lst), 2)
    max_ = max(kamas_lst)
    min_ = min(kamas_lst)

    if mean and max_ and min_:
        backend_post_daily_kamas_value(kamas_dict, mean, max_, min_, server)


def get_kamas_value_from_websites_safully(kamas_dict: dict, name: str, callback: Callable, server: str) -> None:
    try:
        kamas_dict[name] = callback(server)
    except Exception as e:
        print(f"Error while getting kamas value from {name} for server {server}: {e}")