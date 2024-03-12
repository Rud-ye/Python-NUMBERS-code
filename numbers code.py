#armstrong no.
num = int(input("Enter a number: "))
sum = 0
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")

#neon no.
sum = 0
print("Enter the number to check:")
num = int(input())
square = num * num

while (square != 0):
    digit = square % 10
    sum = sum + digit
    square = square // 10

if (num == sum):
    print(str(num) + " is a neon number.")
else:
    print(str(num) + " is not a neon number.")
    
#magic numbers
start = 1
end = 500
list_magic = []
for numb in range(start,end+1):
    if numb % 9 == 1:
        list_magic.append(numb)
print("Magic numbers between 1 and 200: \n",list_magic)

#prime no.
num = 29
flag = False
if num == 1:
    print(num, "is not a prime number")
elif num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            break
    if flag:
        print(num, "is not a prime number")
    else:
        print(num, "is a prime number")

#reverse a no.
num = 1234
reversed_num = 0

while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

print("Reversed Number: " + str(reversed_num))

#abundant no.
import math
n = 12
sum=1 
i=2
while(i<=math.sqrt(n)): 
  if(n%i==0): 
    if(n//i==i):  
      sum=sum+i 
    else: 
        sum=sum + i + n/i 
        i=i+1 
    if(sum>n):
        print(n,"is Abundant Number")
    else:
        print(n,"is not Abundant Number")

#triangular no.
def all_triangle_numbers(n):
    for i in range(1, n + 1):   
        print("n = {0}, triangle = {1}".format(i, (i ** 2 + i)//2))
all_triangle_numbers(10)        

#perfect no.
num=int(input("Enter the number: "))  
sum_v=0  
for i in range(1,num):  
    if (num%i==0):  
        sum_v=sum_v+i  
if(sum_v==num):  
    print("The entered number is a perfect number")  
else:  
    print("The entered number is not a perfect number")  
