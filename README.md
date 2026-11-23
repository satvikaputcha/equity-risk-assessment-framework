# Equity Risk Assessment Framework

### Performance • Risk • Portfolio Analytics

A Python-based portfolio risk and performance analysis project that evaluates a diversified portfolio of six financial assets against the S&P 500 benchmark. The project combines financial data analysis, portfolio risk measurement, statistical analysis, and Power BI visualization.

The objective is to understand not only how a portfolio performs, but also the level of risk involved in achieving those returns.

---

## Project Overview

This project analyses the historical performance and risk characteristics of a hypothetical equally weighted portfolio consisting of six assets across different sectors and asset classes.

The portfolio is evaluated against the SPY ETF, which tracks the S&P 500 and serves as the benchmark.

Historical market data is downloaded using Yahoo Finance. Python and pandas are used for data preparation, return calculations, portfolio construction, and risk measurement. The resulting datasets are exported to Power BI for interactive visualization.

**Analysis period:** January 2017 to the latest available market observation.

**Latest published data observation:** November 12, 2026.

## Portfolio Composition

The portfolio consists of six equally weighted holdings, with each asset representing approximately 16.67% of the portfolio.

| Ticker | Asset | Exposure |
|---|---|---|
| AAPL | Apple Inc. | Technology |
| JPM | JPMorgan Chase | Financial services |
| JNJ | Johnson & Johnson | Healthcare |
| EFA | iShares MSCI EAFE ETF | Developed-market equities |
| LQD | iShares iBoxx $ Investment Grade Corporate Bond ETF | Investment-grade corporate bonds |
| DBC | Invesco DB Commodity Index Tracking Fund | Broad commodities |

**Benchmark:** SPY (SPDR S&P 500 ETF Trust)

SPY is used exclusively as the market benchmark and is not included among the six portfolio holdings.

The assets were selected to introduce different sector and asset-class exposures, allowing an examination of how their historical return and risk characteristics interact within a portfolio.

## Project Objectives

- Collect and prepare historical financial market data.
- Calculate daily and cumulative asset returns.
- Analyse annualized returns and volatility.
- Examine correlations between portfolio holdings and the benchmark.
- Construct an equally weighted hypothetical portfolio.
- Calculate portfolio and individual asset beta.
- Measure downside risk using maximum drawdown and historical Value at Risk (VaR).
- Evaluate risk-adjusted performance using the Sharpe ratio.
- Prepare structured datasets for Power BI.
- Present portfolio and asset-level findings through an interactive dashboard.

---

## Technology Stack

| Tool / Library | Purpose |
|---|---|
| Python | Financial analysis and calculations |
| pandas | Data manipulation and analysis |
| NumPy | Numerical calculations |
| Matplotlib | Data visualization |
| Plotly | Visualization support |
| yfinance | Historical market data retrieval |
| Jupyter Notebook | Analysis workflow |
| FRED | Historical US Treasury yield data |
| Power BI | Interactive dashboard |
| Git and GitHub | Version control and project documentation |

Python dependencies and pinned package versions are provided in `requirements.txt`.

---

## Data Sources and Preparation

### Market Data

Historical market data is retrieved from Yahoo Finance using the `yfinance` library.

- Start date: January 1, 2017.
- End date: Dynamically generated using the current date.
- Price field: Adjusted closing prices, retrieved using `auto_adjust=True`.
- Currency: USD.
- Assets: Six portfolio holdings and one benchmark.

The Yahoo Finance end date is exclusive, so the latest available observation may precede the requested end date.

### Risk-Free Rate

Historical 3-month US Treasury yields are retrieved from the Federal Reserve Economic Data (FRED) database using the `DGS3MO` series.

The annual yield is converted from percentage form into a daily risk-free return using a 252-trading-day convention. The series is aligned with the market return dates, with forward filling used for missing observations.

### Data Preparation

The data preparation process includes:

- Extracting adjusted closing prices.
- Validating expected asset columns.
- Checking missing values and duplicate dates.
- Checking for non-positive prices.
- Verifying chronological ordering.
- Calculating daily percentage returns.
- Removing the initial missing return observation.
- Exporting processed datasets as CSV files.

The reusable market data download function is maintained in `src/data_loader.py`.

---

## Analysis Methodology

### 1. Return Analysis

Daily returns are calculated using percentage changes in adjusted closing prices.

Cumulative returns are calculated by compounding daily returns over the analysis period.

Annualized returns are calculated using the compounded daily return series and a 252-trading-day annualization convention.

### 2. Volatility

Daily volatility is measured using the standard deviation of daily returns.

Annualized volatility is calculated using:

Annualized Volatility = Daily Standard Deviation × √252

### 3. Portfolio Construction

The portfolio uses equal weights across its six holdings.

Each holding receives a weight of approximately 16.67%.

Daily portfolio returns are calculated as the weighted sum of the individual asset returns.

The model assumes constant portfolio weights on a daily basis. It does not simulate actual trades or account for the costs of rebalancing.

### 4. Correlation Analysis

Pearson correlation coefficients are calculated using daily returns.

The correlation matrix is used to examine the strength and direction of historical relationships between assets.

Correlation is a measure of association, not causation, and relationships may change over time.

### 5. Beta

Beta measures an asset's or portfolio's sensitivity to movements in the benchmark.

Individual asset beta and portfolio beta are calculated relative to SPY using covariance divided by benchmark variance.

### 6. Maximum Drawdown

Maximum drawdown measures the largest peak-to-trough decline in the cumulative portfolio value over the analysis period.

The portfolio and SPY drawdowns are calculated independently for comparison.

### 7. Value at Risk (VaR)

Historical 95% daily VaR is calculated using the 5th percentile of daily returns.

It estimates the historical daily loss threshold associated with the lower 5% of observed returns.

VaR is a statistical estimate, not a maximum possible loss or a guarantee of future performance.

### 8. Sharpe Ratio

The Sharpe ratio measures excess return relative to return volatility.

Daily excess returns are calculated by subtracting the aligned daily risk-free rate from daily asset or portfolio returns.

The Sharpe ratio is annualized using a 252-trading-day convention.

---

## Results at a Glance

The following results represent the latest published dataset, with observations through November 12, 2026.

### Portfolio vs. Benchmark

| Metric | Portfolio | SPY |
|---|---:|---:|
| Annualized Return | 14.72% | 14.88% |
| Annualized Volatility | 13.37% | 18.13% |
| Sharpe Ratio | 0.900 | 0.713 |
| Beta | 0.654 | 1.000 |
| Maximum Drawdown | -28.52% | -33.72% |
| 95% Daily VaR | -1.19% | -1.69% |

### Asset-Level Performance

| Asset | Annualized Return | Annualized Volatility | Sharpe Ratio | Beta |
|---|---:|---:|---:|---:|
| AAPL | 30.09% | 29.34% | 0.955 | 1.196 |
| JPM | 18.01% | 27.48% | 0.646 | 1.055 |
| JNJ | 12.52% | 19.12% | 0.578 | 0.433 |
| EFA | 9.21% | 17.14% | 0.450 | 0.801 |
| DBC | 9.01% | 18.02% | 0.426 | 0.286 |
| LQD | 2.30% | 8.74% | 0.008 | 0.152 |
| SPY | 14.88% | 18.13% | 0.713 | 1.000 |

### Key Observations

- The portfolio delivered a historical annualized return of 14.72%, compared with 14.88% for SPY.
- Portfolio annualized volatility was lower than the benchmark's, at 13.37% compared with 18.13%.
- The portfolio recorded a higher Sharpe ratio of 0.900 compared with SPY's 0.713.
- Portfolio beta of 0.654 indicates lower historical sensitivity to benchmark movements.
- Maximum drawdown was smaller for the portfolio (-28.52%) than for SPY (-33.72%).
- The portfolio's historical 95% daily VaR was -1.19%, compared with -1.69% for SPY.
- AAPL recorded the highest annualized return among the six portfolio holdings, while LQD recorded the lowest annualized volatility.

Overall, the portfolio delivered a historical return close to the benchmark while exhibiting lower measured volatility and downside risk over the selected period. These historical observations do not establish future performance or guarantee that the same relationships will persist.

---

## Power BI Dashboard

A single-page Power BI dashboard presents the portfolio's key performance and risk metrics alongside individual asset analysis.

The dashboard includes:

**Portfolio KPI Cards**
- Annualized Return
- Annualized Volatility
- Sharpe Ratio
- Maximum Drawdown
- 95% Daily VaR

**Asset-Level Analysis**
- Annual Return by Asset
- Annual Volatility by Asset
- Sharpe Ratio by Asset
- Beta by Asset

**Portfolio Risk and Relationships**
- Asset Correlation Matrix
- Portfolio Value vs. Running Peak
- Portfolio Drawdown over Time

The dashboard uses the processed CSV files generated by the final analysis notebook.

The Power BI report is available at:

`powerbi/equity_risk_dashboard.pbix`

The dashboard uses the latest exported datasets. Opening the report does not automatically execute the Python notebooks or download updated market data. To update the analysis, rerun the notebooks and refresh the data in Power BI.

---

## Repository Structure

```text
equity-risk-assessment-framework/
│
├── data/
│   ├── raw/
│   └── processed/
│       ├── asset_summary.csv
│       ├── close_prices.csv
│       ├── correlation_long.csv
│       ├── correlation_matrix.csv
│       ├── daily_returns.csv
│       ├── portfolio_history.csv
│       └── portfolio_summary.csv
│
├── notebooks/
│   ├── 01_data_collection.ipynb
│   ├── 02_return_analysis.ipynb
│   ├── 03_risk_metrics.ipynb
│   ├── 04_downside_risk.ipynb
│   ├── 05_risk_adjusted_performance.ipynb
│   └── 06_dashboard_data.ipynb
│
├── src/
│   └── data_loader.py
│
├── powerbi/
│   └── equity_risk_dashboard.pbix
│
├── reports/
│   └── Portfolio Risk and Performance Review.pdf
│
├── tests/
│
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

---

## How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/satvikaputcha/equity-risk-assessment-framework.git

cd equity-risk-assessment-framework
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate the environment in Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
python -m pip install --upgrade pip

pip install -r requirements.txt
```

### 4. Run the Jupyter Notebooks

Open the project in VS Code and select the `.venv` Python environment as the notebook kernel.

The notebooks should be executed in the following order:

1. `01_data_collection.ipynb`
2. `02_return_analysis.ipynb`
3. `03_risk_metrics.ipynb`
4. `04_downside_risk.ipynb`
5. `05_risk_adjusted_performance.ipynb`
6. `06_dashboard_data.ipynb`

**Working directory:** The notebooks use paths relative to the `notebooks` directory. When running them, ensure the notebook working directory is set to that folder so the project paths resolve correctly.

The first notebook downloads market data. Subsequent notebooks use the processed datasets generated by earlier steps.

### 5. Open the Power BI Dashboard

Open:

`powerbi/equity_risk_dashboard.pbix`

The dashboard uses the processed CSV files located in `data/processed/`.

If running the project from a different directory, update the Power BI data-source paths as necessary before refreshing the report.

---

## Assumptions and Limitations

This project is a retrospective analysis of a hypothetical portfolio. It is not investment advice or a live portfolio management system.

The analysis has the following assumptions and limitations:

- The portfolio is equally weighted across six holdings.
- Portfolio weights are treated as constant on a daily basis.
- No transaction costs, taxes, brokerage fees, bid-ask spreads, market impact, or turnover costs are included.
- The analysis uses historical market data, and past performance does not predict future results.
- Asset selection is retrospective, introducing potential selection and hindsight bias.
- The portfolio includes three individual US-listed companies, so company-specific risks remain.
- AAPL's strong historical performance contributes to the portfolio's overall historical results.
- Correlations and volatility can change across market conditions.
- Beta measures historical sensitivity to SPY and does not capture every source of risk.
- Sharpe ratios depend on the selected risk-free rate and annualization assumptions.
- Historical VaR is sample-dependent and does not capture every possible extreme market event.
- VaR exceedances are evaluated using the same historical sample used to estimate the VaR threshold. This is an in-sample consistency check, not independent out-of-sample backtesting.
- The analysis does not incorporate individual investor objectives, liquidity requirements, or risk tolerance.

---

## Potential Future Improvements

- Expected Shortfall (Conditional VaR).
- Rolling volatility and beta analysis.
- Historical market stress testing.
- Portfolio optimization and efficient frontier analysis.
- Alternative portfolio weight allocations.
- Rebalancing frequency comparisons.
- Transaction costs and real-world portfolio constraints.
- Independent out-of-sample VaR backtesting.
- Automated data updates and reporting.
- Expanded automated testing and validation.

---

## Conclusion

The Equity Risk Assessment Framework combines financial data collection, portfolio construction, statistical risk measurement, and interactive visualization into a structured analytical workflow.

By evaluating returns alongside volatility, correlation, beta, drawdowns, VaR, and Sharpe ratios, the project demonstrates how portfolio performance can be assessed in the context of the risks taken to achieve it.

The analysis highlights the importance of looking beyond returns alone when evaluating portfolio performance.

