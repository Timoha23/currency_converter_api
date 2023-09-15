from pydantic import BaseModel


class ConversionData(BaseModel):
    """
    Схема результата конвертации
    """

    success: bool
    query: dict[str, str | int | float] | None
    error: dict[str, str | int] | None
    result: int | float | None
