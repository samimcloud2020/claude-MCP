from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP
import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Initialize FastMCP server
mcp = FastMCP("StockAnalysisServer")

# Tool 1: Fetch current stock price
@mcp.tool()
async def get_stock_price(ticker: str) -> str:
    """
    Fetches the current stock price and volume for a given ticker symbol.
    Args:
        ticker: The stock ticker symbol (e.g., 'AAPL').
    Returns:
        str: Formatted string with the ticker, latest price, volume, and timestamp.
    """
    try:
        stock = yf.Ticker(ticker)
        data = stock.history(period="1d")
        if data.empty:
            return f"No data available for ticker {ticker}."
        latest_price = round(data['Close'].iloc[-1], 2)
        volume = int(data['Volume'].iloc[-1])
        timestamp = data.index[-1].strftime("%Y-%m-%d %H:%M:%S")
        return f"""
Symbol: {ticker}
Latest Price: ${latest_price}
Volume: {volume:,}
Timestamp: {timestamp}
"""
    except Exception as e:
        return f"Error fetching data for {ticker}: {str(e)}"

# Tool 2: Fetch historical stock data
@mcp.tool()
async def get_historical_data(ticker: str, start_date: str, end_date: str = None) -> str:
    """
    Fetches historical stock prices for a given ticker and date range.
    Args:
        ticker: The stock ticker symbol (e.g., 'AAPL').
        start_date: Start date in YYYY-MM-DD format.
        end_date: End date in YYYY-MM-DD format (optional, defaults to today).
    Returns:
        str: Formatted string with the ticker and daily closing prices.
    """
    try:
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d") if end_date else datetime.now()
        stock = yf.Ticker(ticker)
        data = stock.history(start=start, end=end)
        if data.empty:
            return f"No data available for ticker {ticker} in the specified date range."
        formatted_data = [
            f"Date: {index.strftime('%Y-%m-%d')}, Close: ${round(row['Close'], 2)}"
            for index, row in data.iterrows()
        ]
        return f"""
Symbol: {ticker}
Historical Data:
{"\n".join(formatted_data[:10])}  # Limited to 10 entries for brevity
"""
    except Exception as e:
        return f"Error fetching historical data for {ticker}: {str(e)}"

# Tool 3: Calculate financial metrics
@mcp.tool()
async def calculate_metrics(ticker: str, period: str = "1y") -> str:
    """
    Calculates the 20-day simple moving average and annualized volatility for a ticker.
    Args:
        ticker: The stock ticker symbol (e.g., 'AAPL').
        period: Time period for data (e.g., '1mo', '3mo', '1y'). Defaults to '1y'.
    Returns:
        str: Formatted string with the ticker, SMA, volatility, and timestamp.
    """
    try:
        stock = yf.Ticker(ticker)
        data = stock.history(period=period)
        if data.empty:
            return f"No data available for ticker {ticker}."
        sma = data['Close'].rolling(window=20).mean().iloc[-1]
        log_returns = np.log(data['Close'] / data['Close'].shift(1))
        volatility = np.std(log_returns) * np.sqrt(252)
        timestamp = data.index[-1].strftime("%Y-%m-%d %H:%M:%S")
        return f"""
Symbol: {ticker}
20-Day SMA: ${round(sma, 2)}
Annualized Volatility: {round(volatility, 4)}
Timestamp: {timestamp}
"""
    except Exception as e:
        return f"Error calculating metrics for {ticker}: {str(e)}"

# Resource for server version
@mcp.resource("config://version")
def get_version():
    """
    Returns the version of the Stock Analysis MCP server.
    """
    return "1.3.0"

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')