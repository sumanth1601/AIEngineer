marks = int(input("Enter marks: "))

if marks < 0 or marks >= 100:
    print("Invalid Marks")

elif marks >= 90:
    print("Excellent")
elif marks >=75:
    print("Good")
elif marks >=50:
    print("Average")
else:
    print("Need Improvement")


print("Enter the Marks :", marks)