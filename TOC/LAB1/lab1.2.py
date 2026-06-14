def check_prefix(s1,s2):
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

    for i in range(len2):
        if s1[i]!=s2[i]:
            return "Not a Prefix."
        
    if len2==len1:
        return "Following pair of strings is improper prefix."
    else:
        return "Following pair of stirngs is Proper prefix"
    

print("\n--test case 1:Improper prefix")
print(check_prefix("saugat","saugat"))

print("\n--test case2:proper prefix")
print(check_prefix("saugat","sau"))

print("\n--test case 3: Not a prefix")
print(check_prefix("saug","saugattamang"))
