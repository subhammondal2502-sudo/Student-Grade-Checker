#Student Grade Checker.....
students_name=input("enter students name : ")
marks=int(input("enter total marks upto 100 : "))
print(students_name)
print("total marks : ", marks)
if marks<0 or marks>100:
    print("Invalide marks")
