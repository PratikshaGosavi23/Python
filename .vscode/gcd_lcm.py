# Program to find GCD and LCM of two numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Finding GCD
x = a
y = b

while y != 0:
    x, y = y, x % y

gcd = x

# Finding LCM
lcm = (a * b) // gcd

print("GCD of", a, "and", b, "is", gcd)
print("LCM of", a, "and", b, "is", lcm)
