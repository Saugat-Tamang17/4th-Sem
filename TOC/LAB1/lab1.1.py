def is_valid(input_string,allowed_alphabet):
    for char in input_string:
        if char not in allowed_alphabet:
            return False;
    
    return True




alphabet = input("Enter the Alphabet set :")
allowed_alphabet=set(alphabet)
print("Type 'exit' to stop testing strings.\n")

while True:
    user_string=input("Enter the String to test:\n")

    if user_string.lower()=="exit":
        print("Exiting")
        break

    result=is_valid(user_string,allowed_alphabet)
    print(f"String: '{user_string}' -> {'Valid' if result else 'Invalid'}")

