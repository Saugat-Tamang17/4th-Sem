import math

def is_prime(num):
    
    if num <= 1:
        return
        
    if num == 2:
        print(num, end=" ")
        return
    if num % 2 == 0:
        return
    
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return 

    print(num, end=" ")

print("All of the Prime Numbers between 1 and 100 are :\n")
for num in range(1, 101):
    is_prime(num)



    