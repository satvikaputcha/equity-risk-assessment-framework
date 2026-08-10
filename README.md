# Equity Risk Assessment Framework

## Project Overview

The Equity Risk Assessment Framework is a Python-based financial analysis project developed to assess the performance, risk, diversification, and risk-adjusted characteristics of a hypothetical investment portfolio.

The project uses historical market data from January 2016 through July 2026 to analyze a diversified set of equities, an equity market benchmark, gold, and long-duration U.S. Treasury bonds.

The analysis covers daily returns, annualized returns, volatility, correlation, covariance, portfolio returns, beta, Sharpe ratio, drawdown, maximum drawdown, and Value at Risk (VaR).

The project also includes a Power BI dashboard that summarizes and visualizes the key results of the analysis.

## Objectives

The primary objectives of this project are to:

- Evaluate the historical performance of individual assets.
- Measure asset-level risk using volatility.
- Examine relationships between assets using correlation and covariance.
- Construct and evaluate a diversified hypothetical portfolio.
- Measure market sensitivity using beta.
- Assess risk-adjusted performance using the Sharpe ratio.
- Analyze portfolio drawdowns and maximum drawdown.
- Estimate potential daily portfolio losses using 95% Value at Risk (VaR).
- Create a reproducible financial analysis workflow using Python and pandas.
- Present the results through an interactive Power BI dashboard.

## Assets Analyzed

The analysis covers the following assets:

| Ticker | Asset |
|--------|-------|
| AAPL | Apple Inc. |
| JPM | JPMorgan Chase & Co. |
| JNJ | Johnson & Johnson |
| KO | The Coca-Cola Company |
| XOM | Exxon Mobil Corporation |
| SPY | SPDR S&P 500 ETF Trust |
| GLD | SPDR Gold Shares |
| TLT | iShares 20+ Year Treasury Bond ETF |

## Tools & Technologies

The project was developed using the following tools and technologies:

- **Python 3.10.11** – Core programming language used for data collection, processing, financial calculations, and analysis.
- **pandas** – Used for data manipulation, return calculations, statistical analysis, and portfolio computations.
- **NumPy** – Used for numerical calculations and array-based operations.
- **yfinance** – Used to retrieve historical market price data.
- **Jupyter Notebook** – Used to organize and execute the analytical workflow.
- **Git & GitHub** – Used for version control and project management.
- **Power BI** – Used to build the interactive dashboard and visualize portfolio performance and risk metrics.
- **CSV datasets** – Used as supporting data formats for processed financial data and dashboard integration.

## Dataset & Data Preparation

### Data Source

Historical market data was collected using the `yfinance` Python library. The analysis covers the period from **January 2016 through July 2026**.

The dataset contains historical price information for eight assets:

- AAPL
- JPM
- JNJ
- KO
- XOM
- SPY
- GLD
- TLT

Adjusted prices were used as the basis for the return calculations so that historical price movements could be analyzed more consistently.

### Data Preparation

The collected market data was processed using pandas. The main preparation steps included:

1. Downloading historical market data for all selected assets.
2. Selecting the relevant adjusted closing price data.
3. Organizing the prices into a consistent date-indexed time series.
4. Checking the dataset for missing values and data consistency.
5. Calculating daily percentage returns for each asset.
6. Saving the processed datasets as CSV files for subsequent analysis and visualization.

The resulting daily return dataset was used as the foundation for the portfolio construction and risk analysis performed in later stages of the project.

## Methodology & Financial Metrics

The analysis was performed using daily asset returns and progressively built from individual asset statistics to portfolio-level risk measures.

### 1. Daily Returns

Daily returns were calculated from consecutive adjusted closing prices:

$$
R_t = \frac{P_t}{P_{t-1}} - 1
$$

where:

- \(P_t\) is the current day's adjusted closing price.
- \(P_{t-1}\) is the previous trading day's adjusted closing price.
- \(R_t\) is the daily return.

Daily returns provide a standardized measure for comparing the performance of assets with different price levels.

### 2. Annualized Return

Annualized return was used to express historical performance on an annual basis, allowing assets with different cumulative performance to be compared using a common yearly measure.

### 3. Volatility

Volatility was measured using the standard deviation of daily returns.

Daily volatility was annualized using approximately 252 trading days per year:

$$
\sigma_{\text{annual}} = \sigma_{\text{daily}}\sqrt{252}
$$

A higher volatility indicates greater variation in historical returns.

### 4. Correlation

Correlation was used to measure the strength and direction of the linear relationship between asset returns.

The correlation coefficient ranges from -1 to +1:

- +1 indicates a perfect positive relationship.
- 0 indicates no linear relationship.
- -1 indicates a perfect negative relationship.

Correlation was used to evaluate diversification opportunities within the portfolio.

### 5. Covariance

Covariance measures how two assets tend to move together.

Positive covariance indicates that assets tend to move in the same direction, while negative covariance indicates a tendency to move in opposite directions.

Covariance and correlation were used to understand how individual asset movements contribute to overall portfolio risk.

### 6. Portfolio Returns

Portfolio daily returns were calculated as the weighted combination of the individual asset returns:

$$
R_p = \sum_{i=1}^{n} w_iR_i
$$

where:

- \(w_i\) is the portfolio weight of asset \(i\).
- \(R_i\) is the return of asset \(i\).
- \(R_p\) is the portfolio return.

This calculation forms the basis for the portfolio-level performance and risk analysis.

### 7. Beta

Beta was calculated using SPY as the market benchmark:

$$
\beta_i =
\frac{\operatorname{Cov}(R_i,R_m)}
{\operatorname{Var}(R_m)}
$$

Beta measures an asset's sensitivity to movements in the broader market.

- Beta greater than 1 indicates greater market sensitivity.
- Beta between 0 and 1 indicates lower market sensitivity.
- Beta near 0 indicates limited linear market sensitivity.
- Negative beta indicates an inverse relationship with the benchmark.

### 8. Sharpe Ratio

The Sharpe ratio was used to evaluate risk-adjusted performance:

$$
Sharpe =
\frac{R_p-R_f}{\sigma_p}
$$

where:

- \(R_p\) is the portfolio or asset return.
- \(R_f\) is the risk-free rate.
- \(\sigma_p\) is the standard deviation of returns.

A higher Sharpe ratio generally indicates better risk-adjusted performance, as more excess return is generated per unit of volatility.

### 9. Portfolio Value

Portfolio value was calculated by compounding daily portfolio returns from an initial normalized value of approximately 1:

$$
V_t = V_{t-1}(1+R_t)
$$

This produces a time series showing how the portfolio would have evolved over the analysis period.

### 10. Running Maximum

The running maximum represents the highest portfolio value reached up to each point in time:

$$
M_t = \max(V_1,V_2,\ldots,V_t)
$$

The running maximum was used as the reference point for calculating portfolio drawdowns.

### 11. Drawdown

Drawdown measures the percentage decline of the portfolio from its previous peak:

$$
D_t = \frac{V_t-M_t}{M_t}
$$

A drawdown of 0% represents a portfolio at a previous or new high, while negative values indicate a decline from the previous peak.

### 12. Maximum Drawdown

Maximum drawdown is the largest observed decline from a portfolio peak during the analysis period.

The portfolio's maximum drawdown was approximately:

**-26.9%**

This represents the most significant peak-to-trough decline observed in the historical portfolio value series.

### 13. Value at Risk

A 95% daily Value at Risk (VaR) measure was used to estimate a potential daily loss threshold.

The portfolio's estimated 95% daily VaR was approximately:

**-1%**

The result is expressed as a negative return/loss threshold in this analysis. In magnitude terms, this corresponds to approximately **1% of portfolio value**.

## Key Results & Findings

The analysis produced several notable findings across asset performance, risk, diversification, and portfolio-level metrics.

### Asset Performance

Among the eight assets analysed, **AAPL recorded the highest annualised return at approximately 28.29%**.

The approximate annualized return ranking was:

| Rank | Asset | Annualized Return |
|------|-------|------------------:|
| 1 | AAPL | 28.29% |
| 2 | JPM | 20.68% |
| 3 | SPY | 15.15% |
| 4 | GLD | 13.20% |
| 5 | JNJ | 12.32% |
| 6 | XOM | 11.46% |
| 7 | KO | 9.86% |
| 8 | TLT | -0.78% |

AAPL also recorded the highest annualized volatility at approximately **28.92%**, illustrating that its higher historical return was accompanied by greater return variability.

### Asset Risk

The annualized volatility results showed substantial differences between the assets.

AAPL had the highest annualized volatility at approximately **28.92%**, while TLT had the lowest at approximately **14.75%**.

This demonstrates that historical return and risk should be evaluated together rather than considering performance in isolation.

### Market Exposure

Using SPY as the market benchmark, AAPL had the highest beta at approximately **1.20**, followed by JPM at approximately **1.08**.

TLT had a slightly negative beta of approximately **-0.13**, indicating a historically inverse relationship with the benchmark over the analysis period.

### Diversification

The correlation analysis showed that the assets did not move identically.

For example:

- AAPL and SPY had a correlation of approximately **0.74**.
- JPM and SPY had a correlation of approximately **0.70**.
- JPM and TLT had a correlation of approximately **-0.31**.
- SPY and TLT had a correlation of approximately **-0.16**.

The negative relationships observed between TLT and several equity assets indicate potential diversification benefits within a multi-asset portfolio.

### Risk-Adjusted Performance

The portfolio achieved a Sharpe ratio of approximately:

**1.22**

This indicates that the portfolio generated a relatively strong level of return relative to its measured volatility under the assumptions used in the analysis.

Among the individual assets, AAPL ranked highest based on the calculated risk-adjusted performance.

### Portfolio Downside Risk

The portfolio experienced a maximum drawdown of approximately:

**-26.9%**

This represents the largest historical decline from a previous portfolio peak during the analyzed period.

The result highlights why portfolio risk assessment should include downside measures in addition to volatility.

### Value at Risk

The estimated 95% daily portfolio VaR was approximately:

**-1%**

This indicates that, under the assumptions of the selected VaR methodology, losses worse than approximately 1% would be expected to occur in roughly 5% of observations.

VaR was used as a complementary risk measure alongside volatility and maximum drawdown rather than as a standalone measure of portfolio risk.

### Overall Finding

The analysis demonstrates the importance of evaluating investment performance through multiple dimensions.

Although AAPL produced the highest historical return, it also exhibited the highest volatility. Assets such as TLT displayed lower volatility and different market relationships, contributing potential diversification characteristics.

At the portfolio level, the combination of assets produced a Sharpe ratio of approximately **1.22**, while the portfolio's maximum historical drawdown was approximately **-26.9%**.

These results illustrate the trade-off between return, volatility, diversification, and downside risk in portfolio construction.

## Power BI Dashboard

A Power BI dashboard was developed to provide an interactive visual summary of the portfolio analysis.

The dashboard presents key portfolio performance and risk metrics, including:

- Annual return
- Annual volatility
- Sharpe ratio
- Maximum drawdown
- Value at Risk (VaR)
- Asset-level performance comparisons
- Asset volatility comparisons
- Beta analysis
- Asset correlation
- Portfolio drawdown over time

The Power BI report file is available in the `powerbi/` directory:

```text
powerbi/equity_risk_dashboard.pbix
```

## Project Structure

The repository is organized into separate directories for data, analysis notebooks, source code, and dashboard resources.

```text
equity-risk-assessment-framework/
│
├── data/
│   ├── raw/
│   └── processed/
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
├── README.md
├── requirements.txt
└── .gitignore
```


## How to Run the Project

### 1. Clone the Repository

Clone the repository from GitHub:

```bash
git clone https://github.com/satvikaputcha/equity-risk-assessment-framework.git
cd equity-risk-assessment-framework
```

### 2. Create a Virtual Environment

Create a Python virtual environment:

```bash
python -m venv .venv
```

Activate the environment on Windows:

```powershell
.venv\Scripts\activate
```

### 3. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

### 4. Select the Python Environment

When working with the Jupyter notebooks in VS Code, select the project's `.venv` Python environment as the notebook kernel.

### 5. Run the Analysis

Open the notebooks in the `notebooks/` directory and execute them in the following order:

1. `01_data_collection.ipynb` – Collect and prepare historical market data.
2. `02_return_analysis.ipynb` – Calculate and analyze asset returns.
3. `03_risk_metrics.ipynb` – Calculate asset-level and portfolio risk metrics.
4. `04_downside_risk.ipynb` – Analyze portfolio drawdown and downside risk.
5. `05_risk_adjusted_performance.ipynb` – Evaluate risk-adjusted portfolio performance.
6. `06_dashboard_data.ipynb` – Prepare the final datasets used by the Power BI dashboard.

The notebooks follow this general workflow:

```text
Data Collection
      ↓
Data Preparation
      ↓
Return Calculation
      ↓
Asset Analysis
      ↓
Portfolio Construction
      ↓
Risk Analysis
      ↓
Dashboard Data Preparation
```

### 6. Generated Data

The analysis produces processed datasets in:

```text
data/processed/
```

These datasets contain the outputs required for subsequent analysis and visualization.

### 7. Power BI Dashboard

After generating the required processed datasets, the Power BI report can be opened from:

```text
powerbi/equity_risk_dashboard.pbix
```

## Limitations & Assumptions

The results of this project should be interpreted within the following limitations and assumptions:

- The analysis is based on historical market data. Historical performance does not guarantee future results.
- The portfolio is hypothetical and does not represent an actual investment account.
- The analysis period covers January 2016 through July 2026, so conclusions may depend on the specific market conditions observed during this period.
- Volatility is measured using historical standard deviation and does not capture every form of investment risk.
- Correlations between assets are historical and may change during different market conditions.
- Beta is dependent on the selected benchmark, which in this project is SPY.
- The Sharpe ratio depends on the assumptions used for returns, volatility, and the risk-free rate.
- Value at Risk is a statistical estimate and depends on the methodology and assumptions used. Actual losses can exceed the estimated VaR.
- Maximum drawdown describes historical peak-to-trough losses and does not predict future drawdowns.
- The analysis does not account for transaction costs, taxes, brokerage fees, bid-ask spreads, or market impact.
- The portfolio does not model investor-specific objectives, constraints, liquidity requirements, or risk tolerance.

## Future Improvements

The framework can be extended in several ways to provide a more comprehensive assessment of portfolio risk:

- Implement Expected Shortfall (Conditional VaR) to analyze losses beyond the VaR threshold.
- Add rolling volatility and rolling beta to examine how risk changes over time.
- Implement stress testing and scenario analysis for adverse market conditions.
- Explore Monte Carlo simulation for portfolio risk estimation.
- Add portfolio optimization techniques to investigate alternative asset allocations.
- Construct an efficient frontier to compare portfolios across different risk-return combinations.
- Incorporate additional asset classes to further evaluate diversification.
- Include transaction costs, taxes, and other real-world portfolio constraints.
- Automate the process of updating market data and refreshing the analytical outputs.

## Conclusion

This project demonstrates a complete workflow for evaluating the historical risk and performance characteristics of a hypothetical investment portfolio.

The analysis progressed from historical market data and daily return calculations to asset-level performance analysis, portfolio construction, diversification analysis, market exposure, risk-adjusted performance, drawdown analysis, and Value at Risk.

The results highlight the importance of evaluating investments across multiple dimensions rather than relying on return alone. AAPL produced the highest historical annualized return but also experienced the highest volatility, while assets such as TLT displayed lower volatility and different relationships with equity assets.

At the portfolio level, the analysis produced a Sharpe ratio of approximately **1.22** and a maximum drawdown of approximately **-26.9%**, providing complementary measures of risk-adjusted performance and downside risk.

Overall, the project combines Python-based financial analysis with Power BI visualization to create a structured framework for understanding portfolio risk and performance.

