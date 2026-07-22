employee_id = input("Employee ID: ")
employee_name = input("Employee Name: ")
department = input("Department: ")
designation =input("Designation: ")
company_name = input("Company Name: ")
experience_years = int(input("Experience Years: "))
monthly_salary = int(input("Monthly Salary: "),)
official_email = input("Email Address: ")
bonus = int(input("Bonus: "))
annual_salary = monthly_salary * 12


if experience_years >= 10:
    bonus = annual_salary * 20 / 100
elif experience_years >= 5:
    bonus = annual_salary * 10 / 100
else:
    bonus = annual_salary * 5 / 100

final_salary = bonus + annual_salary



print("\n================================================")
print("EMPLOYEE MANAGEMENT SYSTEM")
print("\n================================================")

print(f"Employee ID            :  {employee_id.upper()}")
print(f"Employee Name          :  {employee_name.title()}")
print(f"Department             :  {department.upper()}")
print(f"Designation            :  {designation}")
print(f"Company Name           :  {company_name.upper()}")
print(f"Experience Years       :  {experience_years} 'Years'")

print(f"Monthly Salary         : ₹{monthly_salary:,.0f}",)
print(f"Annual Salary          : ₹{annual_salary:,.0f}")
print(f"Bonus                  : ₹{bonus:,.0f}")
print(f"Final Salary           : ₹{final_salary:,.0f}")

print(f"Official Email         : {official_email}")
print(f"Email Valid            : {official_email.endswith('.com')}")

