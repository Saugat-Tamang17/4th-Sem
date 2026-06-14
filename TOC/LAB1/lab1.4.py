def check_substring(s1,s2):
    len1=0
    len2=0
    for char in s1:
        len1+=1
    
    for char in s2:
        len2+=1

    print(f"the length of the s1 string is :{len1}")
    print(f"The length of the s2 string is :{len2}")

    if len2>len1:
        return "Not a substring since Length of s2 is greater than s1"

    found = False
    for start in range((len1-len2)+1):
        match=True
        for j in range(len2):
            if s1[start+j]!=s2[j]:
                match=False
                break
        
        if match:
            found=True
            break;
    if found:
        if len1==len2:
            return "improper substring"
        else:
            return "proper substring"
        
    else:
        return "not a substring"

    

print("\n--test case 1:Improper substring")
print(check_substring("saugat","saugat"))

print("\n--test case2:proper substring")
print(check_substring("saugat","uga"))

print("\n--test case3:Not a substring")
print(check_substring("saugat","saut"))

print("\n--test case 4: Not a substring")
print(check_substring("saug","saugattamang"))
