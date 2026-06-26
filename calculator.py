def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b


print("===== Calculator =====")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Choose an operation (1-4): ")

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if choice == "1":
    print(f"Result = {add(a, b)}")

elif choice == "2":
    print(f"Result = {subtract(a, b)}")

elif choice == "3":
    print(f"Result = {multiply(a, b)}")

elif choice == "4":
    print(f"Result = {divide(a, b)}")

else:
    print("Invalid choice. Please select between 1 and 4.")