import requests


def backend_get_daily_kamas_value(server: str):
    response = requests.get(url=f"http://127.0.0.1:8000/today?server={server}")
    if response.status_code != 200:
        raise Exception("Endpoint is not available")
    else:
        return response.json()[-1] if response.json() else None


def backend_get_yesterday_kamas_value(server: str):
    response = requests.get(url=f"http://127.0.0.1:8000/yesterday?server={server}")
    if response.status_code != 200:
        raise Exception("Endpoint is not available")
    else:
        return response.json()[-1] if response.json() else None


def backend_get_kamas_value(server: str):
    response = requests.get(url=f"http://127.0.0.1:8000/kamas?server={server}")
    if response.status_code != 200:
        raise Exception("Endpoint is not available")
    else:
        return response.json() or None


def backend_post_daily_kamas_value(values: list, mean: float, max_: float, min_: float, server: str):
    body = {"kamas_dict": values, "average": mean, "max": max_, "min": min_, "server": server}
    response = requests.post(url="http://127.0.0.1:8000/kamas", json=body)
    if response.status_code != 200:
        raise Exception("Endpoint is not available")
