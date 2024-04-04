"""This app does foreign exchange requests"""

from quart import Quart, jsonify, request
from dotenv import load_dotenv
import os

load_dotenv()


app = Quart(__name__)


@app.get("/currencies")
async def currencies_supported():
    currencies = currency_list()
    return jsonify(currencies)


def currency_list():
    """List of currencies supported"""
    currency_list = {"dollar": "USD", "euro": "EUR", "british sterling": "GBP"}
    return currency_list


@app.post("/currency_supported")
async def currency_supported():
    """Tests if the inputted currency is supported"""
    input_currency = await request.get_json()
    currencies = currency_list()
    if currencies.get(input_currency["currency_name"]):
        return "Currency is accepted"
    else:
        return "Currency not supported"


def run() -> None:
    app.run()


if __name__ == "__main__":
    run()
