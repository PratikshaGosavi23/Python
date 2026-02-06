n = int(input("How many numbers: "))
arr = []

for i in range(n):
    arr.append(int(input("Enter number: ")))
    
result = []
    
for x in arr:
    if x not in result:
        result.append(x)
        
print("List after removing duplicates: ", result)
