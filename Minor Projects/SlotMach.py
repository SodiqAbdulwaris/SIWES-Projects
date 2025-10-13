import random

def spin():
    symb = ['🍊', '🍇', '🍎', '🍒', '🍑']    
    results = [random.choice(symb) for i in range(3)]
    return results

def printRow(row):
    print(" | ".join(row))
    print("-----------------------------")

def getPayout(row, BetAmm):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍊':
            return BetAmm * 10
        elif row[0] == '🍇':
            return BetAmm * 5
        elif row[0] == '🍎':
            return BetAmm * 3
        elif row[0] == '🍒':
            return BetAmm * 2
        elif row[0] == '🍑':
            return BetAmm * 1
    return 0

def main():
    bal = 100.00

    print("-----------------------------")
    print("-----------WELCOME-----------")
    print("-----------------------------")
    print("-- Symbols:🍊 🍇 🍎 🍒 🍑 ---")
    print("-----------------------------")
    print(f"------ You have {bal} ------")
    print("-----------------------------")

    while True:       
        if bal == 0:
            print("You are out of money")
            break
        print(f"Current Balance: {bal:.2f}")
        bBetAmm = input("How much do u wanna stake: ")
        if bBetAmm.isdigit() == False:
            print("Invalid Input, Try again")
            continue
        BetAmm = float(bBetAmm)
        if BetAmm <= 0:
            print("Enter Correct Stake: ")
            continue
        if BetAmm > bal:
            print("You don't have enough money")
            continue
        bal -= BetAmm
        print("Spinning...")
        print("")

        row = spin()
        printRow(row)
        payout = getPayout(row, BetAmm)

        if payout > 0:
            print(f"You won {payout}")
            bal += payout
        resp = input("Do you still want to play? (yes/no): ")
        if resp.lower() != "yes":
            print("Thank you for playing!")
            print(f"Your current Balance is {bal:.2f}")
            break

main()
