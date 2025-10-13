
CardNum = int(input("What is your credit card number: ").replace("-", "").replace(" ", ""))


def Validator(CardNum):
    CNS = str(CardNum)
    total = 0
    LenCN = len(CNS)
    remain = []
    for num in reversed(range(0, LenCN)):
        a = int(CNS[num]) * 2       
        if LenCN % 2 == 0:
            if num % 2 != 0:
                remain.append(int(CNS[num]))
                continue
            while a > 9:
                a -= 9
            total += a
        elif LenCN % 2 != 0:
            if num % 2 == 0 or num == 0:
                remain.append(int(CNS[num]))
                continue
            while a > 9:
                a -= 9
            total += a
    for n in remain:
        total += n
    
    if total % 10 == 0:
        print("Valid")
    else:
        print("Invalid") 
    
Validator(CardNum)
