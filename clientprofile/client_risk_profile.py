# Questionary portion to input and calculate the client's risk profile and initial investment

# Please import this to the main app with the following code: #
''' from fileio.clientriskprofile import client_risk_tolerance_info'''

#collect client data for scoring#

def client_risk_tolerance_info():
    
    close_friend = input("A. On a scale of 1(Risky Avoidant) - 4(Risky), how would your closest friend describe your risk tolerance?")
    close_friend =int(close_friend)
    
    self_eval = input("B. On a scale of 1(Risky Avoidant) - 4(Risky), how would you describe your risk tolerance?")        
    self_eval = int(self_eval)
    
    would_you_rather = input("C. What would you rather:" 
    "1. Take $1,000 in cash  "
    "2. A 50% chance at winning $5,000  "
    "3. A 25% chance at winning $10,000  "
     "4. A 5% chance at winning $100,000  ")
    would_you_rather = int(would_you_rather)
    
    risk_define = input(
    "D. Define risk: 1. Loss "
        "2. Uncertainty "
        "3. Opportunity "
        "4. Thrill ")
    risk_define = int(risk_define)
    
    willingness = input("E. How comfortable on a scale of 1(Not Comfortable) - 4(Very Comfortable)"
        "are you with investing your money into stocks?")
    willingness = int(willingness)
    
    return close_friend, self_eval, would_you_rather, risk_define, willingness

# aggregate data for tolerance level #

def aggregate_client_score():
    close_friend, self_eval, would_you_rather, risk_define, willingness = client_risk_tolerance_info()
    return sum([close_friend, self_eval, would_you_rather, risk_define, willingness])

# calculate the risk tolerance level by finding the mean of the score #

def client_risk_tolerance():
    risk_sum = aggregate_client_score()
    if isinstance(risk_sum, int) and 1 <= risk_sum <= 20:
        risk_factor = risk_sum/20
        return (f'Your risk profile is {risk_factor}')
    else:
        risk_factor = risk_sum/20
        return print(f'Your answers are not applicable, please input a value between 1-4 for each question {risk_factor}')  
    