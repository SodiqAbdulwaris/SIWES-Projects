import sqlite3

conn = sqlite3.connect("BankDB.db")
cur = conn.cursor()

cur.execute(
    """
    CREATE TABLE IF NOT EXISTS BankData (
        AccountNumber INTEGER PRIMARY KEY,
        FullName TEXT NOT NULL,
        PhoneNumber TEXT NOT NULL,
        DateofBirth TEXT,
        NextofKin TEXT,
        AccountBalance NUMERIC,
        PinHash VARCHAR(64)
    )
    """
)
conn.commit()

def add_user(AccountNumber, FirstName, LastName, PhoneNumber, DateofBirth, NextofKin, Balance, Pin ):
    FullName = f"{LastName} {FirstName}"
    infoadd = (AccountNumber, FullName, PhoneNumber, DateofBirth, NextofKin, Balance, Pin)
    cur.execute("""
                INSERT INTO BankData(AccountNumber, FullName, PhoneNumber, DateofBirth, NextofKin, AccountBalance, PinHash) 
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """, 
                infoadd)
    conn.commit()
    
    print("Your Account Has Been Created Successfully")

def retrieve_bank_account_name_index():
    cur.execute("""
                SELECT AccountNumber, FullName 
                FROM BankData
                """)
    NumsandNames = cur.fetchall()
    BankIndex = {int(ind[0]): ind[1] for ind in NumsandNames}
    return BankIndex

def retrieve_encoded_pin(AccountNumber):
    cur.execute("""
                SELECT PinHash 
                FROM BankData 
                WHERE AccountNumber = ?
                """, 
                (AccountNumber,))
    Pin = cur.fetchone()
    return Pin[0]

def retrieve_Balance(AccountNumber):
    cur.execute("""
                SELECT AccountBalance 
                FROM BankData 
                WHERE AccountNumber = ?
                """, 
                (AccountNumber,))
    Bal = cur.fetchone()
    return float(Bal[0])

def PhoneNumAccNum():
    cur.execute("""
                SELECT PhoneNumber 
                FROM BankData
                """)
    PNs = cur.fetchall()
    return [PN[0] for PN in PNs]

def AccNums():
    cur.execute("""
                SELECT AccountNumber 
                FROM BankData
                """)
    ANs = cur.fetchall()
    return [int(AN) for AN in ANs]

def ChangePin(NewPinHash, AccountNumber):
    cur.execute("""
                UPDATE BankData SET PinHash = ? WHERE AccountNumber = ?
                """,
    (NewPinHash, AccountNumber, )
    )
    conn.commit()

    

# BankDataDict.update(
#                     {
#                         UserFirstname : {
#                             "Firstname" : UserFirstname,
#                             "Lastname" : UserLastname,
#                             "PhoneNum" : UserPhoneNum,
#                             "Next of Kin" : UserNextofKin,
#                             "Account Number" : UserAccNum,
#                             "Pin" : funcs.pinencrypt(UserPin),
#                             "Balance" : AccBal
#                         }
#                     }
#                 )
