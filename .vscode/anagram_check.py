# Program to check whether two strings are anagrams

str1 = input("Enter frist word: ").lower()
str2 = input("Enter second word: ").lower()

if sorted(str1) == sorted(str2):
    print("Anagram")
else:
    print("Not an Anagram")