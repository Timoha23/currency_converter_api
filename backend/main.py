import uvicorn
from fastapi import APIRouter, FastAPI

from backend.api.handlers import rates_api_router


app = FastAPI(title="CurrencyConverter")

main_api_router = APIRouter(prefix="/api")
main_api_router.include_router(
    rates_api_router,
    prefix="/rates",
    tags=["rates"]
)

app.include_router(main_api_router)

if __name__ == "__main__":
    uvicorn.run(app=app, host="0.0.0.0", port=8000)
