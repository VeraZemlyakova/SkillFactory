import requests
import json
from config import currencies


class ConvertionException(Exception):
    pass


class CryptoConverter:
    @staticmethod
    def get_price(base: str, quote: str, amount: str):
        if quote == base:
            raise ConvertionException(f"Невозможно перевести одинаковые валюты '{base}'.")
        try:
            base_ticker = currencies[base]
        except KeyError:
            raise ConvertionException(f"Не удалось обработать валюту '{base}'.")
        try:
            quote_ticker = currencies[quote]
        except KeyError:
            raise ConvertionException(f"Не удалось обработать валюту '{quote}'.")
        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f"Не удалось обработать количество '{amount}'.")
        else:
            if amount <= 0:
                raise ConvertionException(f"Количество переводимой валюты должно быть больше нуля.")

        r = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={base_ticker}&tsyms={quote_ticker}")
        summ = json.loads(r.content)[currencies[quote]] * amount
        return summ
