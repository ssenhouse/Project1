# Fab Five Portfolio Picker
---
**Columbia University FinTech Bootcamp - Project 1** 
--


# Collaborators
* Sean Senhouse 
* Thomas Magee 
* Ozwald Roche
* Philip Shum
* Jack Hillman

# Motivation
![Custom image using marvel spiderman to illustrate different tech stocks](/images/spiderman_tech_stocks_image.png)

For project 1, our team, "Fab Five Advisors," created a portfolio investment tool based on some of our in-class assignments. However, our professor challenged us to dig deeper and leverage risk parity portfolio theory to develop our tool. With that in mind, we created a tool that takes a client's risk tolerance and asset choices to create a portfolio. The program also uses a Monte Carlo simulation to forecast the future returns of the portfolio. Finally, we created summary statistics and charts to communicate and report our results.

# Technologies

This project leverages python 3.7 specifically and assumes that Jupyter Lab has been installed. In addition, you would need to have the following modules installed:
* pandas
* datetime
* riskfolio
* yfinance
* pathlib

## Custom modules
These modules we leveraged to provide inputs and simulation results:
1. MCSimulation.py - Provided by Columbia FinTech BootCamp

* This module is used to to forecast the future returns of the portfolio over the client's investment horizon.

2. clientprofile.py - Developed by Fab Five Advisors

* 1. Quantify the users risk tolerance by asking the users 5 questions to which they are only allowed to answer with integers 1-4 (otherwise the verifier function forces them to retry). Each answer is then aggregated, and the mean is found to give the client's tolerance an numeric value for their risk tolerance. This variable is passed on to the MCForecastTools.py and the Riskfolio Library for the next process.

* 2. Collect the users input on how long their desired investment time frame is. This variable is used for the Monte Carlo Simulation.

## Installation Guide
### To review Project 1:

* First install the following dependent libraries
```python
pip install riskfolio-lib
pip install yfinance
```

* First initialize the dev environment and the Jupyter lab by typing the following at the command prompt:  

```python
conda activate dev
jupyter lab
```
* Second open the Jupyter Notebook titled: **fab_five_porfolio_picker.ipynb** 

* Run all of the code answering questions on risk tolerance and investment horizon

# Resources

Critical to our completing this project were the following websites. We would recommend that you use these resources. They helped us:
* Understand risk parity portfolio theory and the options within the riskfolio library[https://riskfolio-lib.readthedocs.io/en/latest/index.html]
* Understand how to construct a risk tolerance variable to quantify an investor's appetite for investment risk[https://finmasters.com/risk-profile-test/#gref]
* Source market data on investment assets from yahoo finance, allowing us to create a universe to choose assets quickly [https://github.com/ranaroussi/yfinance]

# Data Collection

When assessing the input data for our risk parity model, we wanted to put an emphasis on risk-diverse assets to include in our "universe".  To do so, our team agreed to include the top 10 individual stocks, ETFs, and bonds ranked by various metrics/sources.

```python
assets = ["XLC", "XLY", "XLP", "XLE", "XLF", "XLV", "XLI", "XLB", "XLRE", "XLK", "XLU", "AAPL", "MSFT", "NVDA", "AMZN", "BRK-B", 
"GOOG", "META", "UNH", "XOM", "AGG", "BND", "LQD", "VCIT", "BNDX", "TMF", "TLT", "ICVT", "LKOR", "FBND"]
```
* Stocks (highest volatility): Top 10 by index weight
* ETFs (medium volatility): Top 10 industry sectors
* Bonds (lowest volatility):  Top 10 bonds to by per money.usnews.com

The diversity in the level of risk of our assets allowed for a larger spread of weight allocation during the optimization stage of the risk model.

# ETL and Cleaning

Yahoo finance formatted their data to provide a relatively painless ETL process.  Using the following lines of code, we were able to download the raw historical data over our desired period of time, extract the specific values required for our analysis, and sort the data by asset instead of by performance measure (opening price, closing price, etc...)

```python
og_data = yf.download(assets, start = start, end = end)
data = og_data.loc[:,('Adj Close', slice(None))]
data.columns = assets

Y = data[assets].pct_change().dropna()
```
![Y_data](/images/Y_data.png)

# Results
To illustrate the results of our model, we ran scenarios to understand the extremes of the model. Specifically, if we are to maximize returns based on the client's risk aversion, how do the results in our portfolio change when the client's risk tolerance is changed?

## Risk Avoidant Client
Based on our questionnaire, the risk-avoidant client would have entered all '1' for the answers to the questions. As a result, the model returned a portfolio that put an emphasis on bonds and sector ETFs, which typically result in low returns and low risk.

## Figure 1

![Risk avoidant optimal porfolio](/images/risk_avoidant_portfolio.png)

## Figure 2

![Risk avoidant optimal portfolio efficient frontier](/images/risk_avoidant_portfolio_efficient_frontier.png)

## Risky Client
Based on our questionnaire, the risky client would have entered all '4' for answers. As a result, the model returned a portfolio that put an emphasis on singular stocks, which result in high returns but also and high risk. 

## Figure 3
![Risky optimal porfolio](/images/risky_portfolio.png)


## Figure 4
![Risky optimal portfolio efficient frontier](/images/risky_portfolio_efficient_frontier.png)

# MonteCarlo Forecast:
Using the weighted assets determined by our risk model, our team forecasted the optimized portfolios over the time horizon inputted by the user (in this case, 10 years).  The results of our forecast for the lowest and highest risk tolerances are below:

## Risk Avoidant Client
The 10 year Monte Carlo forecast predicted, within a 95% confidence interval, that the expected returns will be between 0.78 and 1.41% for the least risk tolerant client.

![Risk avoidant forecast](/images/risk_avoidant_forecast.png)

## Risky Client
The 10 year Monte Carlo forecast predicted, within a 95% confidence interval, that the expected returns will be between 1.08% and 498.69% for the most risk tolerant client.

![Risky forecast](/images/risky_forecast.png)

# Next Steps
One of the exciting outcomes of this project is that there is a long list of options for further analysis and customization of the report. The following is not an exhaustive list but will provide ideas on what other steps can be taken with this project.

**Additional questions**
* Evaluate how to build the universe of investments. For simplicity and to meet our project timeline, we created a static universe comprising a mixed bag of instruments, including stocks, bonds, and ETFs. We did this to ensure not just various companies but asset classes.

* How to best define risk? Specifically, how can we develop a more in-depth analysis for creating the investor profile? As we started to use the model to solve for the optimal portfolio, we observed that the model follows a logarithmic estimation for the optimal portfolio weights. Therefore, we needed to scale our risk aversion factor to see the extremes of the portfolio recommendations based on our universe. Developing a better understanding of this relationship will allow us to quantify the risk tolerance, thus allowing us to create a greater spread of risk tolerance and portfolios.

=======
