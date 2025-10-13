import sqlite3
from datetime import datetime

conn = sqlite3.connect("BankDB.db")
cur = conn.cursor()
cur.execute("PRAGMA foreign_keys = ON")

cur.execute(
    """
    CREATE TABLE IF NOT EXISTS TransactionsData (
        TransactionID INTEGER PRIMARY KEY AUTOINCREMENT,
        AccountNumber INTEGER NOT NULL,
        Type TEXT NOT NULL,
        Amount NUMERIC NOT NULL,
        Description TEXT,
        Time TEXT DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (AccountNumber) REFERENCES BankData(AccountNumber)
    )
    """
)
conn.commit()


def AddTranstoDB(AccountNumber, Type, Amount, Description):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cur.execute(
        """
        INSERT INTO TransactionsData (AccountNumber, Type, Amount, Description, Time)
        VALUES (?, ?, ?, ?, ?)
        """,
        (AccountNumber, Type, Amount, Description, timestamp)
    )
    conn.commit()


def GetTransfromDB(AccountNumber):
    cur.execute(
        """
        SELECT Type, Amount, Description, Time
        FROM TransactionsData
        WHERE AccountNumber = ?
        ORDER BY Time DESC
        """,
        (AccountNumber,)
    )
    return cur.fetchall()

def GetTransbyDate(AccountNumber, StartDate, EndDate):
    cur.execute(
    """
    SELECT Type, Amount, Description, Time 
    FROM TransactionsData
    WHERE AccountNumber = ? AND DATE(Time) BETWEEN DATE(?) AND DATE(?)
    ORDER BY Time DESC
    """,
    (AccountNumber, StartDate, EndDate, )
    )
    return cur.fetchall()