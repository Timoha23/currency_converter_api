from httpx import AsyncClient


async def test_convert_currency(
    async_client: AsyncClient,
):
    """
    Тест конвертации валюты
    """

    good_params = {
        "from_": "USD",
        "to": "RUB",
        "amount": 10,
    }

    bad_params_with_invalid_from = good_params.copy()
    bad_params_with_invalid_from["from_"] = "USDDDD"

    bad_params_with_invalid_to = good_params.copy()
    bad_params_with_invalid_to["to"] = "RUBBBB"

    bad_params_with_invalid_amount = good_params.copy()
    bad_params_with_invalid_amount["amount"] = "A"

    bad_params_without_from = good_params.copy()
    bad_params_without_from.pop("from_")

    # RESPONSES
    # g_r - good response
    # b_r - bad response

    g_r = await async_client.get(
        url="/rates/",
        params=good_params,
    )

    assert g_r.status_code == 200

