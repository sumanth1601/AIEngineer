#=======Assignment 3 - 1 ========
def greet(name):
    print("Hello", name)
greet("Sumanth")
#=======Assignment 3 - 2 ========
def length(string):
    return len(string)
print(length("Python"))
#=======Assignment 3 - 3 ========
def vowel_count(text):
    count = 0
    for char in text.lower():
        if char in "aeiou":
            count += 1

    return count

print(vowel_count("Artificial Intelligence"))