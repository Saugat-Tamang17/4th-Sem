#wap in python to input two numbers and perform sum difference product  quotient and remainder #

n1=float(input("enter the First number:"))
n2=float(input("Enter the Second Number: "))

print(f"\n The first number is :{n1} ")
print(f"\n The second number is :{n2}")

print("\nSum of two numbers:",n1+n2)
print("\nDifference of two numbers:",n1-n2)
print("\nProduct of two numbers:",n1*n2)

if n2==0:
    print("n2 cannot be Zero '0'.")
else:
    print("\nQuotient of two numbers:",n1/n2)
    print("\nRemainder of two numbers:",n1%n2)
