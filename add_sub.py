def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print(f"The addition of {num1} and {num2} is: {add(num1, num2)}")
print(f"The subtraction of {num1} and {num2} is: {subtract(num1, num2)}")