# Moore Machine: counts occurrences of "aab" in a string over {a, b}
# States: q0 (no match), q1 (seen 'a'), q2 (seen 'aa'), q3 (matched 'aab')

def count_aab(s):
    state = 'q0'
    count = 0

    for ch in s:
        if state == 'q0' and ch == 'a':
            state = 'q1'
        elif state == 'q0' and ch == 'b':
            state = 'q0'
        elif state == 'q1' and ch == 'a':
            state = 'q2'
        elif state == 'q1' and ch == 'b':
            state = 'q0'
        elif state == 'q2' and ch == 'a':
            state = 'q2'
        elif state == 'q2' and ch == 'b':
            state = 'q3'
            count += 1
        elif state == 'q3' and ch == 'a':
            state = 'q1'
        elif state == 'q3' and ch == 'b':
            state = 'q0'

    return count


if __name__ == "__main__":
    tests = ["aab", "aabaab", "aaab", "aabb", "ababab", "aabaabaab"]
    for t in tests:
        print(t, "->", count_aab(t))

    user_in = input("\nEnter a string over {a,b}: ")
    print("Occurrences of 'aab':", count_aab(user_in))