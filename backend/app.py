import yfinance as yfinance
from fastapi import FastAPI


lRelevantTickers = ["6RJ0.BE", "NB2.DE", "SDV1.F"]

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Stock Info API!"}

@app.get("/stocks")
def get_stocks(symbols: str):
    ticker_list = [t.strip().upper() for t in symbols.split(",")]
    result = {}
    for ticker in ticker_list:
        try:
            ticker_data = yfinance.Ticker(ticker)
            result[ticker] = {
                "price": ticker_data.info["regularMarketPrice"],
                "currency": ticker_data.info["currency"],
                "change": ticker_data.info["regularMarketChangePercent"]
            }
        except Exception as e:
            result[ticker] = {"error": str(e)}
    return result

@app.get("/health")
def health_check():
    return {"status": "ok"}