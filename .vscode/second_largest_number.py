n = int(input("How many numbers: "))
arr = []

for i in range(n):
    arr.append(int(input("Enter number: ")))
               
unique = list(set(arr))
unique.sort()

print("Second largest number is:", unique[-2])