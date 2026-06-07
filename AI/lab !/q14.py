# Input sentence
sentence = input("Enter a sentence: ") + " "

word = ""
word_count = {}

# Read character by character
for ch in sentence:
    if ch != " ":
        word += ch
    else:
        if word != "":
            word = word.lower()
            
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
            
            word = ""

# Display result
print("\nWord Occurrences:")
for w, count in word_count.items():
    print(w, ":", count)