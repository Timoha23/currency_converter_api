from pydantic import BaseModel


class ConversionResultAmount(BaseModel):
    result: int | float
