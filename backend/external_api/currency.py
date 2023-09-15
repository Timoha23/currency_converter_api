import httpx

from backend.settings import API_KEY, TIMEOUT_FOR_EXTERNAL_API_SECONDS
from backend.external_api.schemas import ConversionData


async def get_conversion_result(
    from_currency: str,
    to_currency: str,
    amount: float,
) -> ConversionData:
    """
    Внешнее API с конвертацией валют.

    ::args
        - from_currency - валюта которую конвертируем
        - to_currency - валюта в которую конвертируем
        - amount - сумма конвертации

    ::return
        - ConversionData - результат конвертации
    """

    timeout = httpx.Timeout(timeout=TIMEOUT_FOR_EXTERNAL_API_SECONDS)

    async with httpx.AsyncClient(timeout=timeout) as client:
        url = 'https://api.apilayer.com/currency_data/convert'
        params = {
            'to': to_currency,
            'from': from_currency,
            'amount': amount,
            'apikey': API_KEY
        }
        currency_json = await client.get(url=url, params=params)
        return currency_json.json()
