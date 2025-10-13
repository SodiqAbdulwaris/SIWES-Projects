import tabulate, datetime, getpass
import BankDB, Transactions, funcs

print("\nWelcome to BMS Bank\n\n")

def menu():
    while True:
        HasAcc = input("Do you have an account(yes/no)? ").lower()
        if HasAcc == "no":
            createacc = input("Do you want to create one(yes/no)? ").lower()
            if createacc == "yes":
                AccBal = 0
                UserFirstname = input("What's your first name? ").title()
                while funcs.ValidName(UserFirstname) != True:
                    print("Invalid name! \nUse only letters, spaces, hyphens, or apostrophes.")
                    UserFirstname = input("What's your first name? ").title()
                
                UserLastname = input("What's your last name? ").title()
                while funcs.ValidName(UserLastname) != True:
                    print("Invalid name! \nUse only letters, spaces, hyphens, or apostrophes.")
                    UserLastname = input("What's your last name? ").title()
                
                
                while True:
                    PNs = BankDB.PhoneNumAccNum()
                    UserPhoneNum = input("What's Your Phone Number(0XXXXXXXXXX)? ")
                    if UserPhoneNum in PNs:
                        print("Phone Number already linked to an account.\nTry with another one.")
                        continue
                    if not funcs.ValidNum(UserPhoneNum):
                        print("Incorrect Format!")
                        continue                 
                    break  
                

                while True:
                    UserDOB = input("what's your Date of Birth (YYYY/MM/DD): ").replace(" ", "")

                    try:
                        year, month, day = UserDOB.split("/")
                        if year.isdigit() != True  or month.isdigit() != True or day.isdigit() != True:
                            print("Date must only be numbers.")
                            continue
                        elif len(year) != 4:
                            print("Invalid Year")
                            continue
                    except ValueError:
                        print("Incorrect Format, Try Again")
                        continue
                        
                    year = int(year)
                    month = int(month)
                    day = int(day)
                    
                    if not (1 <= month <= 12):
                        print("Invalid month. Must be between 1 and 12.")
                        continue
                    if not (1 <= day <= 31):
                        print("Invalid day. Must be between 1 and 31.")
                        continue

                    
                    try:
                        dob = datetime.datetime(year, month, day).date()
                    except ValueError:
                        print("Invalid date. Try Again")
                        continue
                    
                    today = datetime.datetime.today().date()

                    age = today.year - dob.year
                    if (today.month, today.day) < (dob.month, dob.day):
                        age -= 1

                    if age < 18:
                        print("You must be at least 18 to create an account.")
                        return
                    break


                UserNextofKin = input("What's Your Next of Kin's Full name? ")
                UserAccNum = funcs.GenerateAccNo()
                
                while True:
                    UserPin = getpass.getpass("Set a 4-digit PIN: ")
                    if UserPin.isdigit() and len(UserPin) == 4:
                        UserPinConf = getpass.getpass("Enter the Pin again")
                        if UserPin == UserPinConf:
                            break
                        else:
                            print("PINs don't match")
                            continue
                    else:
                        print("PIN must be 4 digits only.")
                
                AccBal += 5000
                UserPin = funcs.pinencrypt(UserPin)
                
                BankDB.add_user(UserAccNum, UserFirstname, UserLastname, UserPhoneNum, UserDOB, UserNextofKin, AccBal, UserPin )
                
                print(f"Your Account Number is {UserAccNum}")
                Transactions.AddTranstoDB(UserAccNum, "Deposit" , 5000, "Initial deposit")
                
            elif createacc == "no":
                print("Okay, Exiting...")
                return
                
            else:
                print("Invalid input, Try again!")
                continue
        elif HasAcc == "yes":
            accno = input("What is your account number? ")
            if not accno.isdigit():
                print("Account number must be digits only.")
                continue

            accno = int(accno)
            BankIndex = BankDB.retrieve_bank_account_name_index()

            if accno not in BankIndex.keys():
                print("Invalid account number.")
                continue

            trials = 0
            while trials < 5:
                accpin = getpass.getpass("Enter your PIN: ")
                AccPin = BankDB.retrieve_encoded_pin(accno)

                if AccPin and funcs.pinencrypt(accpin) == AccPin:
                    while True:
                        print(f"\nWelcome {BankIndex[accno]}")
                        print("1 - View Account Balance")
                        print("2 - Withdraw Money")
                        print("3 - Deposit Money")
                        print("4 - Transfer Funds")
                        print("5 - Transaction History")
                        print("6 - Change Pin")
                        print("7 - Exit\n")

                        try:
                            userop = int(input("Choose operation: "))
                        except ValueError:
                            print("Invalid input, Enter a number from 1 to 7.")
                            continue

                        if userop == 1:
                            print(f"Your balance is ₦{BankDB.retrieve_Balance(accno):.2f}")
                        elif userop == 2:
                                funcs.withdraw(accno)
                                continue
                        elif userop == 3:
                                funcs.deposit(accno)
                                continue
                        elif userop == 4:
                                funcs.transfer(accno)
                                continue
                        elif userop == 5:
                            while True:
                                print("Transactions")
                                print("1. View all Transactions")
                                print("2. View between a specific time period")
                                print("3. Print bank statement(in CSV format)")
                                print("Type EXIT to go back to main menu")
                                TransChoice = input("What do you want to do? ")
                                
                                if TransChoice == "1":
                                    FullTransHist = Transactions.GetTransfromDB(accno)
                                    if FullTransHist is not None:
                                        print("\nTransaction History\n")
                                        print( tabulate.tabulate( FullTransHist, headers=["Type", "Amount", "Description", "Time"], tablefmt="grid"))
                                    else:
                                        print("No transactions found.")
                                elif TransChoice == "2":
                                    
                                    while True:
                                        StartDate = input("What is the start date of the search? (in YYYY-MM-DD) ")
                                        try:
                                            datetime.datetime.strptime(StartDate, "%Y-%m-%d")
                                            break
                                        except ValueError:
                                            print("Invalid format. Please use YYYY-MM-DD.")

                                        
                                    while True:
                                        EndDate = input("What is the end date of the search? (in YYYY-MM-DD) ")
                                        try:
                                            datetime.datetime.strptime(EndDate, "%Y-%m-%d")
                                            break
                                        except ValueError:
                                            print("Invalid format. Please use YYYY-MM-DD.")

                                    
                                    TransHistbyDate = Transactions.GetTransbyDate(accno, StartDate, EndDate)
                                    if TransHistbyDate:
                                        print("\nTransaction History\n")
                                        print( tabulate.tabulate( TransHistbyDate, headers=["Type", "Amount", "Description", "Time"], tablefmt="grid"))
                                    else:
                                        print("No transactions found for this specific time period")
                                    continue
                                    
                                elif TransChoice == "3":
                                    funcs.BankStatement(accno)
                                    print("Succesful")
                                elif TransChoice.upper() == "EXIT":
                                    break
                                else:
                                    print("Wrong Input, Try again")
                                    continue
                            continue
                        elif userop == 6:
                            funcs.ChangePin(accno)
                        elif userop == 7:
                            print("Thanks for banking with us")
                            print("Exiting...")
                            return
                        else:
                            print("Invalid option, try again.")
                else:
                    trials += 1
                    print(f"Wrong PIN. {5 - trials} trials left.")
            else:
                print("Too many failed attempts. Exiting...")
                return

        else:
            print("Wrong input, try again.")

            

menu()
BankDB.conn.close()
