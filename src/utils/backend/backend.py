import requests


def backend_get_daily_kamas_value():
    response = requests.get(url="http://127.0.0.1:8000/today")
    if response.status_code != 200:
        raise Exception("Endpoint is not available")
    else:
        return response.json()[-1] if response.json() else None


def backend_get_yesterday_kamas_value():
    response = requests.get(url="http://127.0.0.1:8000/yesterday")
    if response.status_code != 200:
        raise Exception("Endpoint is not available")
    else:
        return response.json()[-1] if response.json() else None


def backend_get_kamas_value():
    response = requests.get(url="http://127.0.0.1:8000/kamas")
    if response.status_code != 200:
        raise Exception("Endpoint is not available")
    else:
        return response.json() or None


def backend_post_daily_kamas_value(values: list, mean: float, max_: float, min_: float):
    body = {"kamas_dict": values, "average": mean, "max": max_, "min": min_}
    response = requests.post(url="http://127.0.0.1:8000/kamas", json=body)
    if response.status_code != 200:
        raise Exception("Endpoint is not available")
