# Fab Five Porfolio Picker
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

For project 1, our team "Fab Five Advisors", decided to create a portfolio investment tool based on some of our in-class projects. However, our professor challenged us to dig deeper and leverage risk parity portfolio theory to create our tool. With that in mind, we created a tool that takes a client's risk tolerance and asset choices to create a portfolio. The tool also uses a Monte Carlo simulation to forecast the future returns of the portfolio. Finally, we created summary statitics, and charts to communicate and report our results

# Technologies

This project leverages python 3.7 specifically and assumes that jupyter lab has been installed. In additon, you would need to have the following modules installed:
* pandas
* riskfolio
* yfinance
* pathlib

## Custom modules
These modules we leveraged to provide inputs and simulation results
1. MCSimulation.py - Provided by Columbia FinTech BootCamp
2. clientprofile.py - Developed by Fab Five Advisors

## Installation Guide
### To review Project 1:

* First install the following dependent libraries
```python
pip install riskfolio-lib
pip install yfinance
```

* First initialze the dev environment and the Jupyter lab by typing the following at the command prompt:  

```python
conda activate dev
jupyter lab
```
* Second open the Jupter Notebook titled: **fab_five_porfolio_picker.ipynb** 

* Run all of the code answering questions on risk tolerance and investment horizon

# Resources

Critical to us completing this project were the following websites. We recommend that you leverage these resources. They helped us:
* understand risk parity portfolio theory, and the options within the riskfolio library[https://riskfolio-lib.readthedocs.io/en/latest/index.html]
* understand how to construct a risk tolerance variable to quantify an investor's appetite for investment risk[https://finmasters.com/risk-profile-test/#gref]
* source market data on investment assets from yahoo finance allowing us to quickly create a universe to choose assets[https://github.com/ranaroussi/yfinance]

