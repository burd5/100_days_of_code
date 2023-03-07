# Calculator App

# the way we were asked to do it

def divide(n1, n2):
    return n1/n2
def mult(n1, n2):
    return n1 * n2
def sub(n1, n2):
    n1 - n2
def add(n1, n2):
    n1 + n2

operations = {
    "/": divide,
    "+": add,
    "-": sub,
    "*": mult
}

def calculate():
    num1 = int(input("What's the first number?: "))

    for symbol in operations:
        print(symbol)

    should_continue = True

    while should_continue:
        operations_symbol = input("Pick an operation: ")
        num2 = int(input("What's the next number?: "))
        calculation_function = operations[operations_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operations_symbol} {num2} = {answer}")

        response = input(f"Type 'y' to continue calculating with {answer}, 'n' to start with a new calculation, or any other key to exit: ")

        if response == 'y':
            num1 = answer
        elif response == 'n':
            calculate()
        else:
            should_continue = False

calculate()









# my own extremely long way of doing it

"""
operators = ['+', '*', '/', '-']

first_num = int(input("What's the first number?: "))
print("+\n-\n*\n/\n")
operation = input("Pick an operation: ")
while operation not in operators:
    print("That isn't an option")
    operation = input("Pick an operation: ")
sec_num = int(input("What's the next number?: "))

def calculate(first_num, operation, sec_num):
    if operation == '+':
        print(f"{first_num} {operation} {sec_num} = {first_num + sec_num}")
        answer = first_num + sec_num
    elif operation == '*':
        print(f"{first_num} {operation} {sec_num} = {first_num * sec_num}")
        answer = first_num * sec_num
    elif operation == '-':
        print(f"{first_num} {operation} {sec_num} = {first_num - sec_num}")
        answer = first_num - sec_num
    elif operation == '/':
        print(f"{first_num} {operation} {sec_num} = {first_num / sec_num}")
        answer = first_num / sec_num
    
    continue_game = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

    while continue_game == 'y':
        first_num = answer
        print("+\n-\n*\n/\n")
        operation = input("Pick an operation: ")
        while operation not in operators:
            print("That isn't an option")
            operation = input("Pick an operation: ")
        sec_num = int(input("What's the next number?: "))   
        calculate(first_num, operation, sec_num)

    if continue_game == 'n':
        first_num = int(input("What's the first number?: "))
        print("+\n-\n*\n/\n")
        operation = input("Pick an operation: ")
        while operation not in operators:
            print("That isn't an option")
            operation = input("Pick an operation: ")
        sec_num = int(input("What's the next number?: "))
        calculate(first_num, operation, sec_num)


calculate(first_num, operation, sec_num)


"""