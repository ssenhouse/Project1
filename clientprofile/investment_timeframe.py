#module to ask desiredtimeframe to invest"
#please copy and paste into main app#

#ask user for desired timeframe and ensure it is a float value#

investment_timeframe = input("What is the desired timeframe(in # of years) for your investment?")
investment_timeframe = float(investment_timeframe)

#to doublecheck that the variable returns as a float#
type(investment_timeframe)