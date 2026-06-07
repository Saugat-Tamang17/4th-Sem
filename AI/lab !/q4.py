marks=int(input("Enter the Marks:"))
print(f"\n the marks you have obtained is :{marks}")

if marks >=80:
    print("Obtained Distinction Grade.")
elif marks >65 and marks <80 :
    print("Obtained First Division grade.")
elif marks >55 and marks <65:
    print("Obtained Second Division grade.")
elif marks >40 and marks<55:
    print("Obtained Third Division grade.")
else:
    print("Failed")

