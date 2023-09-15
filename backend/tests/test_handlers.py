from httpx import AsyncClient


async def test_convert_currency(
    async_client: AsyncClient,
):
    """
    Тест конвертации валюты
    """

    good_params = {
        "from": "USD",
        "to": "USD",
        "amount": 10,
    }

    bad_params_with_invalid_from = good_params.copy()
    bad_params_with_invalid_from["from"] = "USDDDD"

    bad_params_with_invalid_to = good_params.copy()
    bad_params_with_invalid_to["to"] = "RUBBBB"

    bad_params_with_invalid_amount = good_params.copy()
    bad_params_with_invalid_amount["amount"] = "A"

    bad_params_without_from = good_params.copy()
    bad_params_without_from.pop("from")

    # RESPONSES
    # g_r - good response
    # b_r - bad response

    g_r = await async_client.get(
        url="/rates/",
        params=good_params,
    )
    assert g_r.status_code == 200
    assert g_r.json()["result"] == 10

    b_r_with_invalid_from = await async_client.get(
        url="/rates/",
        params=bad_params_with_invalid_from,
    )
    assert b_r_with_invalid_from.status_code == 422

    b_r_with_invalid_to = await async_client.get(
        url="/rates/",
        params=bad_params_with_invalid_to,
    )
    assert b_r_with_invalid_to.status_code == 422

    b_r_with_invalid_amount = await async_client.get(
        url="/rates/",
        params=bad_params_with_invalid_amount,
    )
    assert b_r_with_invalid_amount.status_code == 422

    b_r_without_from = await async_client.get(
        url="/rates/",
        params=bad_params_with_invalid_amount,
    )
    assert b_r_without_from.status_code == 422
