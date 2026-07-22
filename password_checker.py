password = input("Enter password: ")


if len(password) >= 8:

    print(f"Password Length : {len(password)}")
    print("Result   : Stong Password")

else:
    print("Weak Password")