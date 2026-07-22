employee_name = input("Name: ")
salary = int(input("Salary: "),)
experience = int(input("Experience: "))
bonus = int(input("Bonus: "))


if experience >= 10:
    bonus = salary * 20 / 100
elif experience >= 5:
    bonus = salary * 10 / 100
else:
    bonus = salary * 5 / 100

final_salary = salary + bonus

print("========================================")

print("   EMPLOYEE BONUS REPORT ")
print("========================================")

print(f"Employee Name    : {employee_name}")
print(f"Salary           : ₹{salary:,.0f}",)
print(f"Experience       : {experience} years")
print(f"Bonus            : ₹{bonus:,.0f}")
print(f"Final Salary     : {final_salary:,.0f}")
