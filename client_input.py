# Questionary portion to input and calculate the client's risk profile and initial investment
import questionary
import fire
import pandas as pd
def client_risk_tolerance_info():
    close_friend = questionary.select(
    "On a scale of 1(Risky Avoidant) - 4(Risky), how would your closest friend describe your risk tolerance?",
    choices=[
        "1",
        "2",
        "3",
        "4"
    ]).ask()
    self_eval = questionary.select(
    "On a scale of 1(Risky Avoidant) - 4(Risky), how would you describe your risk tolerance?",
    choices=[
        "1",
        "2",
        "3",
        "4"
    ]).ask()
    would_you_rather = questionary.select(
    "What would you rather 1. Take $1,000 in cash  "
        "2. A 50% chance at winning $5,000  "
        "3. A 25% chance at winning $10,000  "
        "4. A 5% chance at winning $100,000  ",
    choices=[
        "1",
        "2",
        "3",
        "4"
    ]).ask()
    risk_define = questionary.select(
    "Define risk: 1. Loss "
        "2. Uncertainty "
        "3. Opportunity "
        "4. Thrill ",
    choices=[
        "1",
        "2",
        "3",
        "4"
    ]).ask()
    willingness = questionary.select(
    "How comfortable on a scale of 1(Not Comfortable) - 4(Very Comfortable)"
        "are you with investing your money into stocks?",
    choices=[
        "1",
        "2",
        "3",
        "4"
    ]).ask()
    aggregate_risk_tolerance = sum([float(close_friend), float(self_eval), float(would_you_rather), float(risk_define), float(willingness)])
    client_risk_tolerance = aggregate_risk_tolerance/20
    return client_risk_tolerance
client_risk_tolerance = client_risk_tolerance_info()
print(client_risk_tolerance)