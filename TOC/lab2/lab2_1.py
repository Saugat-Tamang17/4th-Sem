def lab2_1_dfa(input_string):
    transition_table = {
        'q0': {'0': 'q1', '1': 'q4'},
        'q1': {'0': 'q2', '1': 'q4'},
        'q2': {'0': 'q3', '1': 'q4'},
        'q3': {'0': 'q1', '1': 'q4'},
        'q4': {'0': 'q1', '1': 'q5'},
        'q5': {'0': 'q1', '1': 'q3'}
    }

    start_state = 'q0' 
    final_state = {'q3'} # Keeping this as a set is perfect for lookup

    # Process the string
    current_state = start_state
    for char in input_string:
        if char not in ['0', '1']:
            return "invalid string"
        
        # Move to the next state from the transition table
        current_state = transition_table[current_state][char]

    if current_state in final_state:
        return "valid"
    else:
        return "invalid"

# FIX 3: Call the main function instead of the nested one
print("first one : 000")
print(lab2_1_dfa("000"))   
print("\second one : 111")   # valid
print(lab2_1_dfa("111"))
print("\nthird one one : 010") 
print(lab2_1_dfa("010"))    
print("\nfourth one : 000111")
  # invalid
print(lab2_1_dfa("000111")) 
print("\nfifth one: 101010 ")  # valid
print(lab2_1_dfa("101010")) 
print("\nsixth one : 0001111")  # invalid
print(lab2_1_dfa("0001111"))  # invalid