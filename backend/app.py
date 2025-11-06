import yfinance as yfinance
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for development; later use specific domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Stock Info API!"}

@app.get("/stock/{symbol}")
def get_stock(symbol: str):
    ticker_data = yfinance.Ticker(symbol)
    result = ticker_data.history(period="1mo")
    return result

@app.get("/health")
def health_check():
    return {"status": "ok"}