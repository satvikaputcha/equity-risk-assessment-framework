
import yfinance as yf
import pandas as pd


def download_market_data(tickers, start_date, end_date):
    """
    Download historical market data from Yahoo Finance.

    Parameters
    ----------
    tickers : list
        List of ticker symbols.
    start_date : str
        Start date in YYYY-MM-DD format.
    end_date : str
        End date in YYYY-MM-DD format.

    Returns
    -------
    pandas.DataFrame
        Historical market data with auto-adjusted prices.

    Raises
    ------
    ValueError
        If the inputs are invalid or no data is returned.
    """
    if not tickers:
        raise ValueError("At least one ticker must be provided.")

    if start_date >= end_date:
        raise ValueError("start_date must be earlier than end_date.")

    data = yf.download(
        tickers=tickers,
        start=start_date,
        end=end_date,
        auto_adjust=True,
        progress=False,
        group_by="ticker"
    )

    if data.empty:
        raise ValueError(
            "No market data was returned. "
            "Check the ticker symbols, date range, and data availability."
        )

    return data
