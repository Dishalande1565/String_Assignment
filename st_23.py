# 23. Check whether a string is a palindrome.

s = input("Enter a string: ")
s = s.lower()
rev = "".join(reversed(s))
if s == rev:
    print("Palindrome")
else:
    print("Not a palindrome")