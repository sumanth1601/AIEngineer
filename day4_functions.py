#==========Assignment4 - 1==============
def is_even(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(is_even(12))
#==========Assignment4 -2 ==============
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))
#==========Assignment4 -3 ==============
def is_palindrome(text):
    return text == text[::-1]
print(is_palindrome("madam"))