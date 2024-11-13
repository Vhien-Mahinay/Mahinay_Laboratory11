ListOfGrades = [] 
Passers = 0

for num in range(5):
    x = float(input("Enter the Student's average Grade:"))
    if x < 40 or x > 100:
        break
    else:
        ListOfGrades.append(x)
        if x >= 75:
            Passers = Passers + 1
if x < 40 or x > 100:
    print("Invalid Input of Grades, Please Try Again")
else: 
    Sum = (ListOfGrades[0]) + (ListOfGrades[1]) + (ListOfGrades[2]) + (ListOfGrades[3]) + (ListOfGrades[4])
    Average = Sum/5
    Passing_Percentage = Passers/5 * 100
    print(f"Average of All Students: {Average}")
    print(f"Passers: {Passers}")
    print(f"% of Students who Passed: {Passing_Percentage}")
    print(f"Grades: {ListOfGrades}")