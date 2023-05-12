# Fab Five Porfolio Picker
---
**Columbia University FinTech Bootcamp - Project 1** 
--

# Collaborators
* Sean Senhouse - link to github repo
* Thomas Magee 
* Ozwald Roche
* Philip Shum
* Jack Hillman

# Motivation
![Custom image using marvel spiderman to illustrate different tech stocks](/images/spiderman_tech_stocks_image.png)

For project 1, our team "Fab Five Advisors", decided to create a portfolio investment tool based on some of our in-class projects. However, our professor challenged us to dig deeper and leverage risk parity portfolio theory to create our tool. With that in mind, we created a tool that takes a client's risk tolerance and asset choices to create a portfolio. The tool also uses a Monte Carlo simulation to forecast the future returns of the portfolio. Finally, we created summary statitics, and charts to communicate and report our results

# Technologies

This project leverages python 3.7 specifically and assumes that jupyter lab has been installed.  in the root directory. In additon, you would need to have the following modules installed:
* pandas
* riskfolio
* yfinance
* pathlib

## Custom modules
* MCSimulation.py - Provided by Columbia FinTech BootCamp
* clientprofile.py - Developed by Fab Five Advisors

## Installation Guide
### To review Project 1:

* First install the following libraries
```python
pip install riskfolio-lib
pip install yfinance
```

* First initialze the dev environment and the Jupyter lab by typing the following at the command prompt:  

```python
str("conda activate dev")
str("jupyter lab")
```
* Open the Jupter Notebook titled: **fab_five_porfolio_picker.ipynb** 
 Ru

