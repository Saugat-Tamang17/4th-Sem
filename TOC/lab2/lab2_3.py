def lab2_3_nfa(input_string):
   
    transition_table = {
        'q0': {'a': {'q0', 'q1'}, 'b': {'q0'}},  # 'a' can stay at q0 OR move to q1
        'q1': {'a': {'q2'}},   
        'q2': {'b': {'q3'}},
        'q3': {'b': {'q4'}},
        'q4': {'a': {'q4'}, 'b': {'q4'}}   # stays in accepting state forever
    }

    start_state = {'q0'}   # defining the start or initial stae 
    final_state = {'q4'}   # defining the final state

    current_states = start_state

    # Process the input string character by character
    for char in input_string:
        if char not in ['a', 'b']:
            return "invalid string (Unknown character)"
        
        next_states = set()
        # Find all possible next states for every currently active state
        for state in current_states:
            if char in transition_table[state]:
                # Combine all possible destinations into our next_states set
                next_states.update(transition_table[state][char])
                
        current_states = next_states

    # If any of our final active states match the accepting state, it's valid
    if current_states.intersection(final_state):
        return "valid"
    else:
        return "invalid"

# --- Test Cases ---
print("\ntesting :aabb")
print(lab2_3_nfa("aabb")) 

print("\ntesting :baabbb")      
print(lab2_3_nfa("baabbb"))   
print("\ntesting :baaabbs")  # valid (contains aabb)
print(lab2_3_nfa("baaabbs"))
print("\ntesting :baba")    # invalid string (contains 's')
print(lab2_3_nfa("baba")) 
print("\ntesting :aaabb")      # invalid (does not contain aabb)
print(lab2_3_nfa("aaaabb"))     # valid (ends with aabb)