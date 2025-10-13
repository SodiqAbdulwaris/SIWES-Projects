def convert_temperature():
    while True:
        temptype = input("Enter the temperature type (°F/°C/K): ").strip().lower()

        if temptype == "f" or "°f":
            temptype2 = input("Enter the temperature type you want to convert to (°C/K): ").strip().lower()
            temp = float(input("Enter temperature in °F: "))
            if temptype2 == "c" or "°c":
                converted = (temp - 32) * 5/9
                print(f"{temp}°F is {converted:.2f}°C")
                break
            elif temptype2 == "k" or "°k":
                converted = (temp - 32) * 5/9 + 273.15
                print(f"{temp}°F is {converted:.2f}K")
                break
            else:
                print("Invalid input. Please enter either '°C' or 'K'.")

        elif temptype == "c" or "°c":
            temptype2 = input("Enter the temperature type you want to convert to (°F/K): ").strip().lower()
            temp = float(input("Enter temperature in °C: "))
            if temptype2 == "f" or "°f":
                converted = (temp * 9/5) + 32
                print(f"{temp}°C is {converted:.2f}°F")
                break
            elif temptype2 in "k" or "°k":
                converted = temp + 273.15
                print(f"{temp}°C is {converted:.2f}K")
                break
            else:
                print("Invalid input. Please enter either '°F' or 'K'.")

        elif temptype == "k" or"°k":
            temptype2 = input("Enter the temperature type you want to convert to (°F/°C): ").strip().lower()
            temp = float(input("Enter temperature in K: "))
            if temptype2 == "f" or "°f":
                converted = (temp - 273.15) * 9/5 + 32
                print(f"{temp}K is {converted:.2f}°F")
                break
            elif temptype2 == "c" or "°c":
                converted = temp - 273.15
                print(f"{temp}K is {converted:.2f}°C")
                break
            else:
                print("Invalid input. Please enter either '°F' or '°C'.")

        else:
            print("Invalid input. Please enter either '°F', '°C', or 'K'.")

convert_temperature()
