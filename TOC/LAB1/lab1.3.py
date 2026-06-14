def check_suffix(s1,s2):
    len1=0
    len2=0
    for char in s1:
        len1+=1
    
    for char in s2:
        len2+=1

    print(f"the length of the s1 string is :{len1}")
    print(f"The length of the s2 string is :{len2}")

    if len2>len1:
        return "Not a Prefix since Length of s2 is greater than s1"

    for i in range(1,len2+1):
        if s1[len1-i]!=s2[len2-i]:
            return "Not a Suffix."
        
    if len2==len1:
        return "Following pair of strings is improper suffix."
    else:
        return "Following pair of stirngs is Proper suffix"
    

print("\n--test case 1:Improper suffix")
print(check_suffix("saugat","saugat"))

print("\n--test case2:proper suffix")
print(check_suffix("saugat","gat"))

print("\n--test case3:Not a suffix")
print(check_suffix("saugat","sau"))

print("\n--test case 4: Not a suffix")
print(check_suffix("saug","saugattamang"))
