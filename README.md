# Crypto Portfolio 
### The purpose of this dataset 

# Source 

## Client Profile Module

This module is used to:

* 1. Quantify the users risk tolerance by asking the users 5 questions to which they are only allowed to answer with integers 1-4 (otherwise the verifier function forces them to retry). Each answer is then aggregated and the mean is found to give the client's tolerance an numeric value for their risk tolerance. This variable is passed on to the MCForecastTools.py and the Riskfolio Library for the next process.

* 2. Collect the users input on how long their desired investment time frame is. This variable is used for the Monte Carlo Simulation.

## Technologies

This project leverages python 3.7 with the following packages:

## Usage

To use the clientprofile module, simply run all code blocks by answering the questions.