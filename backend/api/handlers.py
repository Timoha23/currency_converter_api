from asyncio.exceptions import TimeoutError

from fastapi import APIRouter, HTTPException, Query

from backend.api.schemas import ConversionResultAmount
from backend.external_api.currency import get_conversion_result


rates_api_router = APIRouter()


@rates_api_router.get(path="/", response_model=ConversionResultAmount)
async def convert_currency(
    from_: str = Query(alias="from"),
    to: str = Query(),
    amount: float = Query(),
):
    """
    Конвертация валют.

    :args
        - from_ - валюта которую конвертируем
        - to - валюта в которую конвертируем
        - amount - сумма конвертации

    :return
        - {"result": float} - результат ковертации

    """

    try:
        conversion_result = await get_conversion_result(
            from_currency=from_,
            to_currency=to,
            amount=amount
        )

        if conversion_result.get("success") is False:
            status_code = conversion_result.get("error").get("code")
            detail = conversion_result.get("error").get("info")
            raise HTTPException(
                status_code=status_code,
                detail=detail,
            )
    except TimeoutError:
        raise HTTPException(
            status_code=504,
            detail="Превышенно время ожидаения ответа от "
                   "сервера: https://api.apilayer.com"
        )

    result = conversion_result.get("result")

    return ConversionResultAmount(result=result)
