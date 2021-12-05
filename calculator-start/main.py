#calculator
from replit import clear
from art import logo 

def calculator():
    print(logo)  
    #Addition
    def addition(number1, number2):
        return number1 + number2

    #Substract
    def subtraction(number1, number2):
        return number1 - number2

    #Multiply
    def multiplication(number1, number2):
        return number1 * number2

    #Division
    def division(number1, number2):
        return number1 / number2

    operations_dictionaty = {
        "+": addition,
        "-": subtraction,
        "*": multiplication,
        "/": division
    }

    number1 = float(input("What's the first number?: "))
    for operator in operations_dictionaty:
        print(operator)
    operator_symbol = input("Pick an operator from line above: ")
    number2 = float(input("What's the second number?: "))
    calculation_function = operations_dictionaty[operator_symbol]
    answer = calculation_function(number1, number2)
    print(f"{number1} {operator_symbol} {number2} = {answer}")

    continue_calculation = True
    while continue_calculation:
        yes_no = input(f"type 'y' to continue calculating with {answer} or type 'n' to start a new calculation: ")
        if yes_no == "n":
            continue_calculation = False
            clear()
            calculator()
        else:
            operator_symbol = input("Pick an operation: ")
            next_number = float(input("What's the next number?: "))
            calculation_function = operations_dictionaty[operator_symbol]
            continue_answer = calculation_function(answer, next_number)
            print(
                f"{answer} {operator_symbol} {next_number} = {continue_answer}"
            )
            answer = continue_answer


calculator()
