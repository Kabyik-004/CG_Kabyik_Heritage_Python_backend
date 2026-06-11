student =input("Enter the name of the student: ")
marks = int(input("Enter the marks of the student: "))

if marks >= 85 and attendance >= 90:
    print(student + " is eligible for the scholarship.")
else:   
    print(student + " is not eligible for the scholarship.")
