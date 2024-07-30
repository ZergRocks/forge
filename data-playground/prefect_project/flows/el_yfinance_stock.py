from datetime import datetime

import pandas as pd
import pytz
import yfinance as yf
from deltalake import DeltaTable, write_deltalake
from prefect import flow, get_run_logger


@flow
def backfill_yfinance_data(ticker_symbol: str):
    # logger
    logger = get_run_logger()

    # datetime
    korean_tz = pytz.timezone("Asia/Seoul")
    now_utc = datetime.now(pytz.utc)
    now_korean = now_utc.astimezone(korean_tz)
    timestamp = now_korean.isoformat()
    today = now_korean.date().isoformat()

    # stock
    data = yf.download(ticker_symbol, start="1950-01-01", end=today)
    data["crawled_at"] = timestamp
    data["ticker_symbol"] = ticker_symbol
    logger.info("[DOWNLOAD DONE]")
    logger.info(data.head())
    write_deltalake(
        "./.deltalake/yfinance/stock",
        data,
        mode="append",
        schema_mode="merge",
        engine="rust",
    )
    dt = DeltaTable("./.deltalake/yfinance/stock")
    logger.info("[WRITE DONE]")
    logger.info(dt.to_pandas().head())

    # dividends
    data = pd.DataFrame(yf.Ticker(ticker_symbol).dividends)
    data["crawled_at"] = timestamp
    data["ticker_symbol"] = ticker_symbol
    logger.info("[DOWNLOAD DONE]")
    logger.info(data.head())
    write_deltalake(
        "./.deltalake/yfinance/dividends",
        data,
        mode="append",
        schema_mode="merge",
        engine="rust",
    )
    dt = DeltaTable("./.deltalake/yfinance/dividends")
    logger.info("[WRITE DONE]")
    logger.info(dt.to_pandas().head())

    # splits
    data = pd.DataFrame(yf.Ticker(ticker_symbol).splits)
    data["crawled_at"] = timestamp
    data["ticker_symbol"] = ticker_symbol
    logger.info("[DOWNLOAD DONE]")
    logger.info(data.head())
    write_deltalake(
        "./.deltalake/yfinance/splits",
        data,
        mode="append",
        schema_mode="merge",
        engine="rust",
    )
    dt = DeltaTable("./.deltalake/yfinance/splits")
    logger.info("[WRITE DONE]")
    logger.info(dt.to_pandas().head())

    # financials
    data = yf.Ticker(ticker_symbol).financials.T
    data["crawled_at"] = timestamp
    data["ticker_symbol"] = ticker_symbol
    logger.info("[DOWNLOAD DONE]")
    logger.info(data.head())
    write_deltalake(
        "./.deltalake/yfinance/financials",
        data,
        mode="append",
        schema_mode="merge",
        engine="rust",
    )
    dt = DeltaTable("./.deltalake/yfinance/financials")
    logger.info("[WRITE DONE]")
    logger.info(dt.to_pandas().head())

    # balance_sheet
    data = yf.Ticker(ticker_symbol).balance_sheet.T
    data["crawled_at"] = timestamp
    data["ticker_symbol"] = ticker_symbol
    logger.info("[DOWNLOAD DONE]")
    logger.info(data.head())
    write_deltalake(
        "./.deltalake/yfinance/balance_sheet",
        data,
        mode="append",
        schema_mode="merge",
        engine="rust",
    )
    dt = DeltaTable("./.deltalake/yfinance/balance_sheet")
    logger.info("[WRITE DONE]")
    logger.info(dt.to_pandas().head())

    # cash_flow
    data = yf.Ticker(ticker_symbol).cash_flow.T
    data["crawled_at"] = timestamp
    data["ticker_symbol"] = ticker_symbol
    logger.info("[DOWNLOAD DONE]")
    logger.info(data.head())
    write_deltalake(
        "./.deltalake/yfinance/cash_flow",
        data,
        mode="append",
        schema_mode="merge",
        engine="rust",
    )
    dt = DeltaTable("./.deltalake/yfinance/cash_flow")
    logger.info("[WRITE DONE]")
    logger.info(dt.to_pandas().head())

    # earnings
    data = pd.DataFrame(yf.Ticker(ticker_symbol).earnings_dates)
    data["crawled_at"] = timestamp
    data["ticker_symbol"] = ticker_symbol
    logger.info("[DOWNLOAD DONE]")
    logger.info(data.head())
    write_deltalake(
        "./.deltalake/yfinance/earnings",
        data,
        mode="append",
        schema_mode="merge",
        engine="rust",
    )
    dt = DeltaTable("./.deltalake/yfinance/earnings")
    logger.info("[WRITE DONE]")
    logger.info(dt.to_pandas().head())


if __name__ == "__main__":
    backfill_yfinance_data("AAPL")
