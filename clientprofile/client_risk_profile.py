# Questionary portion to input and calculate the client's risk profile and initial investment

# Please import this to the main app with the following code: #
''' from fileio.clientriskprofile import client_risk_tolerance_info'''

#collect client data for scoring#

def verifier(text):
    while True:
        variable = input(text) 
        if variable == "1" or variable == "2" or variable == "3" or variable == "4":
            return variable
            break
        else:
            print("Please enter a valid input")

def client_risk_tolerance_info():   
    
    close_friend = verifier("A. On a scale of 1(Risky Avoidant) - 4(Risky), how would your closest friend describe your risk tolerance?")
    close_friend =float(close_friend)
    
    self_eval = verifier("B. On a scale of 1(Risky Avoidant) - 4(Risky), how would you describe your risk tolerance?")        
    self_eval = float(self_eval)
    
    would_you_rather = verifier("C. What would you rather:" 
    "1. Take $1,000 in cash  "
    "2. A 50% chance at winning $5,000  "
    "3. A 25% chance at winning $10,000  "
     "4. A 5% chance at winning $100,000  ")
    would_you_rather = float(would_you_rather)
    
    risk_define = verifier(
    "D. Define risk: 1. Loss "
        "2. Uncertainty "
        "3. Opportunity "
        "4. Thrill ")
    risk_define = float(risk_define)
    
    willingness = verifier("E. How comfortable on a scale of 1(Not Comfortable) - 4(Very Comfortable)"
        "are you with investing your money into stocks?")
    willingness = float(willingness)
        
    return close_friend, self_eval, would_you_rather, risk_define, willingness
        
# aggregate data for tolerance level #

def aggregate_client_score():
    close_friend, self_eval, would_you_rather, risk_define, willingness = client_risk_tolerance_info()
    return sum([close_friend, self_eval, would_you_rather, risk_define, willingness])

# calculate the risk tolerance level by finding the mean of the score #

def client_risk_tolerance():
    risk_sum = aggregate_client_score()
    if isinstance(risk_sum, float) and 1 <= risk_sum <= 20:
        return risk_sum / 20
    else:
        return print("Your answers are not applicable, please input a value between 1-4 for each question")
