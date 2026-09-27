def display_menu():
    print("\n===== Calculator Menu =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    print("============================")

def get_numbers():
    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            return num1, num2
        except ValueError:
            print("Invalid input. Please enter numeric values.")

def add(a, b):
    return a + b

def subtract(a, b):
    # Returns the difference between two numbers
    return a - b

def multiply(a, b):
    # Returns the product of two numbers
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

def main():
    while True:
        display_menu()
        choice = input("Choose an option (1-5): ")

        if choice == "5":
            print("Exiting calculator. Goodbye!")
            break
        elif choice not in ["1", "2", "3", "4"]:
            print("Invalid choice. Please select 1-5.")
            continue

        num1, num2 = get_numbers()

        if choice == "1":
            print(f"Result: {add(num1, num2)}")
        elif choice == "2":
            print(f"Result: {subtract(num1, num2)}")
        elif choice == "3":
            print(f"Result: {multiply(num1, num2)}")
        elif choice == "4":
            print(f"Result: {divide(num1, num2)}")

if __name__ == "__main__":
    main()