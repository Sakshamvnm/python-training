#Wap to print correspending grades to gpa provided bv user.
name =input("Enter student's name:")
print(f"Name:{name}")
marks=input("Enter your obtained grades(A+,A,B+,B,C):")
if marks=="A+":
    print("You got above 3.6 GPA.")
elif marks=="A":
    print("You got above 3.2 GPA.")
elif marks=="B+":
    print("You got above 2.6 GPA.")
elif marks=="B":
    print("You got above 2.4 GPA.")
elif marks=="C":
    print("You failed:")
else :
    print("The GPA you have entered is invalid:")
