age = int(input("Enter your age: "))
salary = int(input("Enter your salary: "))
credit_score = int(input("Enter your credit Score: "))


if age >= 21 and salary >= 30000 and credit_score >=750:
    print("Loan Approved")
else:
    print("Loan Rejected")
