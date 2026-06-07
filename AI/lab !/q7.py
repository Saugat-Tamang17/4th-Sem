# Program to count vowels and consonants in a string

string = input("Enter a string: ").lower()

vowels = 0
consonants = 0

for ch in string:
    if ch.isalpha():  # Check if character is a letter
        if ch in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Number of vowels:", vowels)
print("Number of consonants:", consonants)