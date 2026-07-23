

employee_id = input("Employee ID: ")
employee_name = input("Employee Name: ")
age = int(input("Age: "))
department = input("Department: ")
designation =input("Designation: ")
company_name = input("Company Name: ")
experience_years = int(input("Experience Years: "))
salary = int(input("Monthly Salary: "),)
official_email = input("Email Address: ")
annual_salary = salary * 12
bonus = int(input("Bonus Years: "))
final_salary = annual_salary + bonus



#Bonus Calculation

if experience_years >= 10:
    bonus = annual_salary * 20 / 100

elif experience_years >= 5:
    bonus = annual_salary * 10 / 100

else:
    bonus = annual_salary * 5 / 100

#Tax Calculation

if final_salary >= 1500000:
    tax_catergory ="High Tax"
else:
    tax_catergory ="Normal Tax"


#Age Calculation
if  18 <= age <= 25:
    category = "Junior"

elif 26 <= age <= 40:
    category = "Mid Level"

else:
    category = "Senior"



print("\n ====================================================")

print("                 EMPLOYEE PAYROLL SYSTEM")

print("====================================================")


print(f"Employee ID            :  {employee_id}")
print(f"Employee Name          :  {employee_name.upper()}")
print(f"Age                    :  {age}")
print(f"Category               :  {category.title()}")



print(f"Department             :  {department.upper()}")
print(f"Designation            :  {designation.title()}")
print(f"Company Name           :  {company_name.upper()}")

print(f"Experience Years       :  {experience_years}")

print(f"Monthly Salary         :  ₹{salary:,.0f}")
print(f"Annual Salary          :  ₹{annual_salary:,.0f}")
print(f"Bonus                  :  ₹{bonus:,.0f}")
print(f"Final Salary           :  ₹{final_salary:,.0f}")
print(f"Tax category           :  {category.title()}")


print(f"Official Email         :  {official_email}")
print(f"Email Status           :  {official_email.endswith('.com') and official_email.__contains__('@')}")


print(f"Name Length            :  {len(employee_name)}")
print(f"Count of 'a'           :  {employee_name.count('a')}")
print(f"First Space            :  {employee_name.find(' ')}")
print(f"Modified Name          :  {employee_name.replace(' ', '_')}")