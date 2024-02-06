def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def divide(num1, num2):
    return num1 / num2 if num2 != 0 else print("can't divide by zero")

def multiply(num1, num2):
    return num1 * num2

def power(num1, num2):
    return num1 ** num2

sign_mapper = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "^": power,
}



def execute_expression(exp):
    num1_text, sign, num2_text = exp.split()
    num1 = float(num1_text)
    num2 = float(num2_text)

    return sign_mapper[sign](num1, num2)





expression = input()

result = execute_expression(expression)
print(f"{result:.2f}")