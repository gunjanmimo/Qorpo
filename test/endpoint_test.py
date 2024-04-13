import requests
import pytest

BASE_URL = "http://0.0.0.0:8000"


def test_get_price():

    # WITH VALID CURRENCY
    currency = "BTC-USDT"
    endpoint = f"{BASE_URL}/price/{currency}"
    print(endpoint)
    response = requests.get(endpoint)
    assert response.status_code == 200
    data = response.json()
    assert "currency" in data
    assert "price" in data
    assert "date" in data
    assert data["currency"] == currency
    # WITH INVALID CURRENCY
    currency = "UNKNOWN_CURRENCY"
    endpoint = f"{BASE_URL}/price/{currency}"
    print(endpoint)
    response = requests.get(endpoint)
    assert response.status_code == 400
    data = response.json()
    assert "message" in data


def test_get_price_history():
    response = requests.get(f"{BASE_URL}/price/history")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data["data"], list)


def test_delete_price_history():
    response = requests.delete(f"{BASE_URL}/price/history")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Price history deleted successfully"
    # CHECK IF PRICE HISTORY IS EMPTY
    response = requests.get(f"{BASE_URL}/price/history")
    data = response.json()
    assert len(data["data"]) == 0
