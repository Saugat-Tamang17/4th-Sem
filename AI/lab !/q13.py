n=int(input("enter how many inputs you want:"))
numbers=[]

for i in range(n):
  num=int(input(f"enter input{i+1}:"))
  numbers.append(num)

  even_numbers=list(filter(lambda x:x%2==0,numbers))


print("Original list:", numbers)
print("Even numbers:", even_numbers)