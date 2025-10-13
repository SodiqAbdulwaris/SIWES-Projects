import BankDB, Transactions
import hashlib, re, random, csv, os, getpass

def pinencrypt(pin):
    pin = str(pin)
    return hashlib.sha256(pin.encode()).hexdigest()

def ValidName(name):
    if name.isalpha():
        pattern = r"^[A-Za-z][A-Za-z\s\-']{1,49}$"
        return re.match(pattern, name) is not None
    
def ValidNum(PhoneNumber):
    PhoneNumber = PhoneNumber.replace(" ", "")
        
    pattern = r"^0(70|80|81|90|91)\d{8}$"
    match = bool(re.match(pattern, PhoneNumber))
    return match

def GenerateAccNo():
    while True:
        AccountNumbers = BankDB.retrieve_bank_account_name_index().keys()
        UserAccNum = int(f"615{random.randint(1000000, 9999999)}")
        if UserAccNum not in AccountNumbers:
            return UserAccNum

def BankStatement(AccountNumber):
    BankIndex = BankDB.retrieve_bank_account_name_index()
    FullTransHists = Transactions.GetTransfromDB(AccountNumber)
    
    if not os.path.exists("Docs"):
        os.mkdir("Docs")
    with open(f"Docs\\{BankIndex[AccountNumber]} Transaction Docs.csv", "w", newline="", encoding="utf-8-sig") as TransHistFile:
        writer = csv.writer(TransHistFile)
        writer.writerow(["Type", "Amount", "Description", "Time"])
        for FullTransHist in FullTransHists:
            writer.writerow(FullTransHist)
    
    
def withdraw(AccountNumber):
    
    
    bal = BankDB.retrieve_Balance(AccountNumber)
    while True:
        amount = input("How much do you want to withdraw? ")

        if amount.replace(",", "").isdigit():
            amount = float(amount)
            if bal - amount < 1000:
                print("Withdrawal denied!.\nBalance cannot go below ₦1,000.00")
                Transactions.AddTranstoDB(AccountNumber, "Withdrawal", amount, f"Failed to withdraw ₦{amount:.2f}")
                continue

            elif amount < bal:
                if amount >= 10000:
                    newbal = bal - amount - 50
                    Transactions.AddTranstoDB(AccountNumber, "Charges", 50, "Charged ₦50.00 for transactions exceeding ₦10,000.00")
                else:
                    newbal = bal - amount
                BankDB.cur.execute(
                    "UPDATE BankData SET AccountBalance = ? WHERE AccountNumber = ?",
                    (newbal, AccountNumber)
                )
                BankDB.conn.commit()
                Transactions.AddTranstoDB(AccountNumber, "Withdrawal", amount, f"Successfully Withdrew ₦{amount:.2f}")
                print(f"You have withdrawn ₦{amount:.2f}")
                
                break
            else:
                print("Insufficient balance")
                continue
        else:
            print("Please enter a valid amount.")
            continue

def transfer(sender_accno):
    print("\nBank Transfer System")

    BankIndex = BankDB.retrieve_bank_account_name_index()

    if sender_accno not in BankIndex:
        print(f"Error: {sender_accno} is not registered in bank database.")
        return
    else:
        print(f"Sender: {BankIndex[sender_accno]}")

    receiver_accno = input("Enter receiver's account number: ")
    receiver_accno = receiver_accno.replace(",", "")
    if not receiver_accno.isdigit():
        print("Receiver account must be digits only.")
        return
    receiver_accno = int(receiver_accno)

    if receiver_accno not in BankIndex:
        print(f"Error: {receiver_accno} is not registered in bank database.")
        return
    else:
        print(f"Receiver: {BankIndex[receiver_accno]}")

    amount = input("Enter amount to transfer: ")
    if not amount.isdigit():
        print("Invalid amount.")
        return
    amount = float(amount)

    SenderBal = float(BankDB.retrieve_Balance(sender_accno))
    ReceiverBal = float(BankDB.retrieve_Balance(receiver_accno))

    if SenderBal - amount < 1000:
        print("Transfer failed: Balance cannot go below 1000.")
        Transactions.AddTranstoDB(sender_accno, "Transfer", amount, f"Failed to Transfer ₦{amount} to {receiver_accno} due to insufficient balance.")
        return
    
    SenderBal -= amount
    if amount >= 10000:
        ReceiverBal += amount - 50
        Transactions.AddTranstoDB(receiver_accno, "Charges", 50, "Charged ₦50.00 for transactions exceeding ₦10,000.00")
        
    else:
        ReceiverBal += amount

    

    BankDB.cur.execute(
        "UPDATE BankData SET AccountBalance = ? WHERE AccountNumber = ?",
        (SenderBal, sender_accno)
    )
    BankDB.cur.execute(
        "UPDATE BankData SET AccountBalance = ? WHERE AccountNumber = ?",
        (ReceiverBal, receiver_accno)
    )
    BankDB.conn.commit()

    Transactions.AddTranstoDB(sender_accno, "Transfer", amount, f"Transfered ₦{amount:.2f} to {BankIndex[receiver_accno]}")
    Transactions.AddTranstoDB(receiver_accno, "Deposit", amount - 50, f"Recieved ₦{amount:.2f} from {BankIndex[sender_accno]}")
    
    print(f"\nTransfer successful! ₦{amount:.2f} sent from {BankIndex[sender_accno]} to {BankIndex[receiver_accno]}.")
    print(f"Your new balance is ₦{SenderBal:.2f}")
            
def deposit(accno):

    amount = input("How much do you want add to your account? ")
    while amount.isdigit() != True:
        print("Wrong Input")
        amount = input("How much do you want add to your account? ")
    amount = float(amount)
    
    if amount >= 10000:
        amount -= 50
        Transactions.AddTranstoDB(accno, "Charges", 50, "Charged ₦50.00 for transactions exceeding ₦10,000.00")
        
    else: 
        amount
            
    UserBal = float(BankDB.retrieve_Balance(accno))
    UserBal += amount
    BankDB.cur.execute(
        "UPDATE BankData SET AccountBalance = ? WHERE AccountNumber = ?",
        (UserBal, accno)
    )
    BankDB.conn.commit()
    
    Transactions.AddTranstoDB(accno, "Deposit", amount, f"Deposited ₦{amount:.2f} to {accno}")
    print(f"Successfully Deposited ₦{amount} to {accno}")


def ChangePin(accno):
    trials = 0
    print("Change your pin here")
    while trials < 5:
        newpin = getpass.getpass("\nWhat do you want to set as your new pin?")
        if newpin.isdigit() and len(newpin) == 4:
            confirmpin = getpass.getpass("Confirm your new pin")
            if confirmpin.isdigit() and len(confirmpin) == 4:
                if newpin == confirmpin:
                    OldPin = getpass.getpass("Enter your Old Password")
                    OldPinHashIn = pinencrypt(OldPin)
                    OldPinHashDB = BankDB.retrieve_encoded_pin(accno)
                    if OldPinHashIn == OldPinHashDB:
                        newpinhash = pinencrypt(newpin)
                        BankDB.ChangePin(newpinhash, accno)
                        return True
                    else:
                        print("Incorrect Pin")
                        trials += 1
                        print(f"{5 - trials} trials left")
                        continue
                else:
                    print("Pins don't match, Try again")
                    continue
            else:
                print("Pin Must be 4 digits only")
        else:
            print("Pin must be 4 digits only")
            
    print("Too Many Attempts, Try Again!")
    return False