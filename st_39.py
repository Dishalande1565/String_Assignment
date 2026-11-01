# 39. Check whether a string is a valid identifier.


s = input("Enter a string: ")
if s.isidentifier():
    print("Valid identifier")
else:
    print("Not a valid identifier")