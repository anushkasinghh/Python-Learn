from colorama import init
from termcolor import colored

init()

print(colored(" ...AQI CALCULATOR...", color="cyan", attrs=["bold", "dark"]))


def aqi_calc(P, C_P):
    I_high = 0
    I_low = 0
    C_high = .0
    C_low = 0

    S = colored('SENSITIVE GROUPS :', color="cyan", attrs=["bold", "dark"])
    H = colored(
        'HEALTH EFFECT STATEMENTS :',
        color="cyan",
        attrs=[
            "bold",
            "dark"])
    C = colored(
        'CAUTIONARY STATEMENTS :',
        color="cyan",
        attrs=[
            "bold",
            "dark"])

    P = input("Select a pollutant: ")
    C_P = float(input("Enter the concentration of the pollutant in ug/m^3 : "))

    if P == "PM 2.5":
        if C_P <= 12.0:
            I_high += 50.0
            I_low += 0.0
            C_high += 12.0
            C_low += 0.0
            I_P = round((I_high - I_low) / (C_high - C_low)
                        * (C_P - C_low) + I_low, 3)
            category = colored(
                "GREEN", color="green", attrs=[
                    "bold", "dark", "underline", "reverse"])
            print(f" AQI : {I_P} \n AQI category : {category}")
            print(f"{S} People with respiratory or heart disease, the elderly and children are the groups most at risk.\n{H} None\n{C} None")
    if P == "PM 2.5":
        if C_P >= 12.1 and C_P <= 35.4:
            I_high += 100
            I_low += 51
            C_high += 35.4
            C_low += 12.1
            I_P = round((I_high - I_low) / (C_high - C_low)
                        * (C_P - C_low) + I_low, 3)
            category = colored(
                "MODERATE", color="yellow", attrs=[
                    "bold", "dark", "underline", "reverse"])
            print(f" AQI : {I_P} \n AQI category : {category}")
            print(f"{S} People with respiratory or heart disease, the elderly and children are the groups most at risk.\n{H} Unusually sensitive people should consider reducing prolonged or heavy exertion.\n{C} Unusually sensitive people should consider reducing prolonged or heavy exertion.")
    if P == "PM 2.5":
        if C_P >= 35.5 and C_P <= 55.4:
            I_high += 150
            I_low += 101
            C_high += 55.4
            C_low += 35.5
            I_P = round((I_high - I_low) / (C_high - C_low)
                        * (C_P - C_low) + I_low, 3)
            category = colored(
                "UNHEALTHY FOR SENSITIVE GROUPS",
                color="white",
                attrs=[
                    "bold",
                    "dark",
                    "underline",
                    "reverse"])
            print(f" AQI : {I_P} \n AQI category : {category}")
            print(f"{S} People with respiratory or heart disease, the elderly and children are the groups most at risk.\n{H} Increasing likelihood of respiratory symptoms in sensitive individuals, aggravation of heart or lung disease and premature mortality in persons with cardiopulmonary disease and the elderly.\n{C} People with respiratory or heart disease, the elderly and children should limit prolonged exertion.")

    if P == "PM 2.5":
        if C_P >= 55.5 and C_P <= 150.4:
            I_high += 200
            I_low += 151
            C_high += 150.4
            C_low += 55.5
            I_P = round((I_high - I_low) / (C_high - C_low)
                        * (C_P - C_low) + I_low, 3)
            category = colored(
                "UNHEALTHY", color="red", attrs=[
                    "bold", "dark", "underline", "reverse"])
            print(f" AQI : {I_P} \n AQI category : {category}")
            print(f"{S} People with respiratory or heart disease, the elderly and children are the groups most at risk.\n{H} Increased aggravation of heart or lung disease and premature mortality in persons with cardiopulmonary disease and the elderly; increased respiratory effects in general population.\n{C} People with respiratory or heart disease, the elderly and children should avoid prolonged exertion; everyone else should limit prolonged exertion.")

    if P == "PM 2.5":
        if C_P >= 150.5 and C_P <= 250.4:
            I_high += 300
            I_low += 201
            C_high += 250.4
            C_low += 150.5
            I_P = round((I_high - I_low) / (C_high - C_low)
                        * (C_P - C_low) + I_low, 3)
            category = colored(
                "VERY UNHEALTHY", color="blue", attrs=[
                    "bold", "dark", "underline", "reverse"])
            print(f" AQI : {I_P} \n AQI category : {category}")
            print(f"{S} People with respiratory or heart disease, the elderly and children are the groups most at risk.\n{H} Significant aggravation of heart or lung disease and premature mortality in persons with cardiopulmonary disease and the elderly; significant increase in respiratory effects in general population.\n{C} People with respiratory or heart disease, the elderly and children should avoid any outdoor activity; everyone else should avoid prolonged exertion.")

    if P == "PM 2.5":
        if C_P >= 250.5 and C_P <= 500.4:
            I_high += 500
            I_low += 301
            C_high += 500.4
            C_low += 250.5
            I_P = round((I_high - I_low) / (C_high - C_low)
                        * (C_P - C_low) + I_low, 3)
            category = colored(
                "HAZARDOUS", color="magenta", attrs=[
                    "bold", "dark", "underline", "reverse"])
            print(f" AQI : {I_P} \n AQI category : {category}")
            print(f"{S} People with respiratory or heart disease, the elderly and children are the groups most at risk.\n{H} Serious aggravation of heart or lung disease and premature mortality in persons with cardiopulmonary disease and the elderly; serious risk of respiratory effects in general population.\n{C} Everyone should avoid any outdoor exertion; people with respiratory or heart disease, the elderly and children should remain indoors.")


aqi_calc("PM 2.5", 10)