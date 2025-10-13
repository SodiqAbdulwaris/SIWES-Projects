print("Weight Converter")
weight = input("What are you converting from? (lbs or kg) ")

if (weight.lower() == "lbs" or weight.lower() == "pounds"):
    weight = input("Enter weight in lbs: ")
    weight = float(weight)
    converted = weight * 0.45
    print(f"Weight in kg: {converted:.2f}")
elif weight == "kg":
    weight = input("Enter weight in kg: ")
    weight = float(weight)
    converted = weight * 2.20
    print(f"Weight in lbs: {converted:.2f}kg")
else:
    print("Invalid input. Please enter either 'lbs' or 'kg'")
