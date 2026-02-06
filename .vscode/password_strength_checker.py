password = input("Enter password: ")

upper = lower = digit = 0

for ch in password:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
    elif ch.isdigit():
        digit += 1

if len(password) >= 8 and upper > 0 and lower > 0 and digit > 0:
    print("Strong Password ✅")
else:
    print("Weak Password ❌")
