#Program to check whether a number is an Armstrong number

num = int(input("Enter a number: "))
temp = num
sum = 0

digits = len(str(num))

while temp > 0:
    digit = temp % 10
    sum = sum + digit ** digits
    temp = temp // 10
    
if num == sum:
    print(num, "is an Armstrong number")        
else:
    print(num, "is not an Armstrong number")