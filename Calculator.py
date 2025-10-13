

while True:
    print("-----------------------")
    print("--------Welcome--------")
    print("What do you want to do?")
    print("1. Addition -> +")
    print("2. Subtraction -> -")
    print("3. Multiplication -> x")
    print("4. Division -> /")
    print("5. Remainder -> %")
    print("'stop' to exit")
    print("-----------------------")
    print("\n\n")
    operation = input("Write the number of the operation you want to perform? ")
    if operation.lower() == "stop":
        print("Stopping...")
        break
    if operation.isdigit() == False or 1 >= int(operation) >= 5:
        print("Invalid Input, Try again")
        continue
    
    num1 = input("What is your first number? ")
    num2 = input("What is your second number? ")
    
    if num1.isdigit() and num2.isdigit():
        num1 = int(num1)
        num2 = int(num2)
    else:
        print("Input must be a number")
        continue
        
    
    
    if operation == "1":
        result = f"{num1} + {num2} = {num1 + num2}"
    elif operation == "2":
        result = f"{num1} - {num2} = {num1 - num2}"
    elif operation == "3":
        result = f"{num1} * {num2} = {num1 * num2}"
    elif operation == "4":
        if num2 != 0:
            result = f"{num1} / {num2} = {num1 / num2}"
        else:
            result = f"{num1} / {num2} = undefined"
    elif operation == "5":
        result = f"{num1} % {num2} = {num1 % num2}"
    else:
        result = "Invalid Input"
    print(result)
    continue

