def run_modulo_dfa(binary_string):
    # Define start state: (rem_0, rem_1)
    # The state tracks: (count of 0s % 3, count of 1s % 3)
    state = (0, 0)
    
    # Track overall absolute counts to handle the "non-zero" requirement
    c0, c1 = 0, 0
    
    for char in binary_string:
        if char not in {'0', '1'}:
            print("Invalid Input")
            return False
        
        rem_0, rem_1 = state
        if char == '0':
            c0 += 1
            # Transition rule for reading '0': increment remainder of 0s modulo 3
            state = ((rem_0 + 1) % 3, rem_1)
        elif char == '1':
            c1 += 1
            # Transition rule for reading '1': increment remainder of 1s modulo 3
            state = (rem_0, (rem_1 + 1) % 3)
            
    rem_0, rem_1 = state
    
    # Check final accepting state requirements
    is_accepted = (rem_0 == 0 and c0 > 0) or (rem_1 == 0 and c1 > 0)
    
    if is_accepted:
        print("String Accepted")
    else:
        print("String Rejected")
        
    return is_accepted


# --- Test Run ---
if __name__ == "__main__":
    test_inputs = ["111", "000", "101", "01010", "111111"]
    for s in test_inputs:
        print(f"Testing '{s}': ", end="")
        run_modulo_dfa(s)