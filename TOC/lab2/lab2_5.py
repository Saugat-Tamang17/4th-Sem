# Mealy Machine: Binary Incrementer  (alphabet a=0, b=1)
# States: S = start, O = carry still active, Z = carry absorbed (copy)

def increment(s):
    s = s.replace('0', 'a').replace('1', 'b')   # accept 0/1 too
    bits = s[::-1]          # read least-significant bit first
    state = 'S'
    out = ''

    for ch in bits:
        if state == 'S' and ch == 'a':
            out += 'b'; state = 'Z'
        elif state == 'S' and ch == 'b':
            out += 'a'; state = 'O'
        elif state == 'O' and ch == 'a':
            out += 'b'; state = 'Z'
        elif state == 'O' and ch == 'b':
            out += 'a'; state = 'O'
        elif state == 'Z':
            out += ch                       # just copy

    if state == 'O':                        # carry overflowed
        out += 'b'

    return out[::-1]


if __name__ == "__main__":
    tests = ["b", "ba", "aa", "bb", "bab", "bbb"]
    for t in tests:
        print(t, "->", increment(t))

    user_in = input("\nEnter a binary string (a/b or 0/1): ")
    print("Incremented:", increment(user_in))