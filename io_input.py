def reverse(text):
    return text[::-1]

def is_palindrome(text):
    return text == reverse(text)

something = input("Enter text: ")

for char in something:
    if char in " ?.!/;:,'":
        something = something.replace(char, '')

print(something)

if is_palindrome(something):
    print("Yes, it is a palindrome")
else:
    print("No, it is not a palindrome")
