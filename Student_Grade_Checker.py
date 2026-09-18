#Student Grade Checker.....
students_name=input("enter students name : ")
marks=int(input("enter total marks upto 100 : "))
print(students_name)
print("total marks : ", marks)
if marks<0 or marks>100:
    print("Invalide marks")

elif marks>=90 :
    print("grade : A")

elif marks>=75 and marks<=89 :
    print("grade : B")

elif marks>=50 and marks<=74 :
    print("grade : c")
