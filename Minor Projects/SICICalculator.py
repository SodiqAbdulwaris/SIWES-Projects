import math

InterestType = input("Enter the type of interest (simple/compound): ").lower()

def CompoundInterest(p, r, t):
    CI = math.pow(p * (1 + r / 100), t) 
    return CI

def SimpleInterest(p, r, t):
    SI = p * r * t / 100
    return SI


while InterestType not in ["simple", "compound", "s", "c", "ci", "si"]:
    print("TRY AGAIN")
    InterestType = input("Enter the type of interest (simple/compound): ").lower()


p = float(input("What is the principal: "))
r = float(input("What is the rate of interest: "))
t = float(input("How long: "))

if InterestType in ["simple", "s", "si"]:
        print(f"The simple interest of {p} over {t} years at {r}% is {SimpleInterest(p, r, t)}")
elif InterestType == ["compound", "c", "ci"]:
        print(f"The compound interest of {p} over {t} years at {r}% is {CompoundInterest(p, r, t)}")


