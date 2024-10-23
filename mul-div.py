def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error! Division by zero is not allowed."

num1 = int(input("Enter your number: "))
num2 = int(input("Enter your number: "))

print(f"The multiplication of {num1} and {num2} is: {multiply(num1, num2)}")
print(f"The division of {num1} by {num2} is: {divide(num1, num2)}")