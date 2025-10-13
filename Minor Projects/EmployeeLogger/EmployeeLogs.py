def EmployeeInfo():
    with open("Employee.txt", "a") as file:
        name = input("What is the employee name? ").strip()
        address = input("What is the employee address? ").strip()
        email = input("What is the employee email? ").strip()
        dept = input("What is the employee department? ").strip()

        if not name or not address or not email or not dept:
            print("Invalid Input! All fields are required.")
        else:
            file.write(f"{name} Details\n")
            file.write(f"   Name: {name}\n")
            file.write(f"   Address: {address}\n")
            file.write(f"   Email: {email}\n")
            file.write(f"   Department: {dept}\n")
            file.write("\n")
            print("Employee information saved successfully!")

EmployeeInfo()
