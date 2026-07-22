email = input("Enter your Email: ")

print("=======STRING METHODS=========")

print(f"Original Email   : {email}")
print(f"Lowercase Email  : {email.lower()}")
print(f"Replace '@'      : {email.replace('@','[at]')}")
print(f"Starts with 'S'  : {email.startswith('s')}")
print(f"Ends with '.com' : {email.endswith('.com')}")
print(f"Count of 'a'     : {email.count('a')}")
print(f"Position of @    : {email.find('@')}")

