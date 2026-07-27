def is_palindrome(num):
    if num == num[::-1]:
        return True
    else:
        return False

print(is_palindrome("python"))