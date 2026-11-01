# 27. Check whether a word exists in a sentence.

sentence = input("Enter a sentence: ")
word = input("Enter a word to search: ")
if word in sentence.split():
    print("Word found")
else:
    print("Word not found")