import re
from typing import List

import numpy as np
import requests
from bs4 import BeautifulSoup

from src.utils.backend.backend import (backend_get_daily_kamas_value,
                                       backend_get_yesterday_kamas_value,
                                       backend_post_daily_kamas_value)


def get_kamas_price_from_kamas_facile_endpoint():
    url = "https://www.kamasfacile.com/fr/boune"
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


def get_kamas_price_from_fun_shop():
    url = "https://www.funshopes.com/purchaseServers.php?lang=fr&g=17"
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception("Endpoint is not available")

    soup = BeautifulSoup(response.text, "html.parser")
    product_prices = soup.find_all("span", class_="prc")
    kamas_value = product_prices[0].text
    kamas_value = kamas_value.split("\\")[0]

    return float(kamas_value)


def get_kamas_price_from_leskamas():
    url = "https://www.leskamas.com/vendre-des-kamas.html"
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception("Endpoint is not available")

    soup = BeautifulSoup(response.text, "html.parser")
    re_pattern = r"<td>Boune<\/td>\s*<td>(.*?)<\/td>"
    match = re.search(re_pattern, str(soup))
    return float(match[1].replace("€/M", ""))


def get_daily_kamas_value():
    if response := backend_get_daily_kamas_value():
        return response


def get_yesterday_kamas_value():
    if response := backend_get_yesterday_kamas_value():
        return response


def get_current_kamas_value():
    kamas_dict = {"Kamas facile": get_kamas_price_from_kamas_facile_endpoint()}
    kamas_dict["Fun shop"] = get_kamas_price_from_fun_shop()
    kamas_dict["Les kamas"] = get_kamas_price_from_leskamas()

    kamas_lst = list(kamas_dict.values())
    mean = round(np.mean(kamas_lst), 2)
    max_ = max(kamas_lst)
    min_ = min(kamas_lst)

    backend_post_daily_kamas_value(kamas_dict, mean, max_, min_)

    return kamas_dict
