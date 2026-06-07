square =lambda x:x*x

greater=lambda a,b:a if a > b else b


num1 = int(input("Enter the first number:"))
num2=int(input("enter the second number:"))

print("Square of 1st Num:",square(num1))
print("Square of 2nd Num:",square(num2))

print("Larger Between two numbers:",greater(num1,num2))