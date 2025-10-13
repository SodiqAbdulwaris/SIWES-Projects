import tabulate

def SchGradeCalc(StudName, StudScore, Summ=None):
    if Summ is None:
        Summ = []
    
    if StudScore.isdigit() and 0 <= int(StudScore) <= 100:
        StudScore = int(StudScore)
        
        if 80 <= StudScore <= 100:
            grade = "A"
        elif 65 <= StudScore <= 79:
            grade = "B"
        elif 55 <= StudScore <= 64:
            grade = "C"
        elif 50 <= StudScore <= 54:
            grade = "D"
        elif 45 <= StudScore <= 49:
            grade = "E"
        else:
            grade = "F"
        
        Summ.append((StudName, StudScore, grade))
        return Summ[-1]
    
    elif not StudScore.isdigit():
        print("Input must be a number within 0 and 100")
    else:
        print("Input must be within 0 and 100")

    return None


print("School Grade Calculator")
Summary = []

while True:
    print("\nTo exit, type 'exit' as student name.")
    print("To view summary table, type 'view' as student name\n")
    StudentName = input("What is the student's name? ")
    
    if StudentName.lower() == "exit":
        print("Exiting...")
        break
    
    if StudentName.lower() == "view":
        print("\nSummary:")
        print(tabulate.tabulate(Summary, headers=["Name", "Score", "Grade"], tablefmt="grid"))
        continue
    
    StudentScore = input("What is the student's score? ")
    
    result = SchGradeCalc(StudentName, StudentScore)
    if result:
        Summary.append(result)


