import xml.etree.ElementTree as ET

import aiohttp

from service_config import RATES_URL


async def get_exchange_rates():
    async with aiohttp.ClientSession() as session:
        async with session.get(RATES_URL) as rates:
            rates_text = await rates.text()
            return rates_text


def parser(data):
    tree = ET.ElementTree(ET.fromstring(data))
    root = tree.getroot()
    rates = {}
    for currency in root.findall("Valute"):
        char_code = currency.find("CharCode").text
        value_unit_rate = float(
            currency.find("VunitRate").text.replace(",", ".")
        )
        rates[char_code] = value_unit_rate
    return rates
