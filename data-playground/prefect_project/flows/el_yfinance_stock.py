import pandas as pd
import yfinance as yf
from deltalake import write_deltalake
from prefect import flow, task


@task
def extract(ticker: str) -> pd.DataFrame:
    stock = yf.Ticker(ticker)
    hist = stock.history(period="1mo")
    return hist


@task
def load(ticker: str, data: pd.DataFrame):
    write_deltalake(
        f"./.deltalake/yfinance_stock/{ticker}",
        data,
        mode="append",
        schema_mode="merge",
        engine="rust",
    )


@flow
def el_yfinance_stock(ticker: str):
    data = extract(ticker)
    load(ticker, data)


if __name__ == "__main__":
    el_yfinance_stock("AAPL")
