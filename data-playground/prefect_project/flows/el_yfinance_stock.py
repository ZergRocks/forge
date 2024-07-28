import yfinance as yf
import json
from prefect import flow, task
from prefect.deployments import Deployment
from prefect.server.schemas.schedules import CronSchedule

@task
def extract(ticker: str):
    stock = yf.Ticker(ticker)
    hist = stock.history(period="1d")
    return hist.to_json(orient="records")

@task
def load(data: dict, filename: str):
    with open(filename, 'w') as f:
        json.dump(data, f)

@flow
def el_yfinance_stock(ticker: str, filename: str):
    stock_data = extract(ticker)
    load(stock_data, filename)


if __name__ == "__main__":
    el_yfinance_stock("AAPL", "yfinance_stock.json")

# # Deployment with a Cron Schedule
# deployment = Deployment.build_from_flow(
#     flow=el_yfinance_stock,
#     name="el_yfinance_stock",
#     parameters={"ticker": "AAPL", "filename": "stock_data.json"},
#     schedule=CronSchedule(cron="0 * * * *")  # 매 정시에 실행
# )
#
# if __name__ == "__main__":
#     deployment.apply()
