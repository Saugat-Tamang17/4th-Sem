n1=int(input("\nEnter the Number:"))
print(f"\n the number you have inputted is :{n1}")
factorial=1

for i in range(1,n1+1):
    factorial=factorial*i

print(f"The factorial of {n1} is {factorial}")