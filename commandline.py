import sys
n=len(sys.argv)
print("Total argument passed:",n)
print("\nName of python script:",end=" ")
print("\nArguments Passed:",end="")
for i in range(1,n):
    print(sys.argv[i],end=" ")

sum=0

for i in range(1,n):
    sum += int(sys.argv[i])

print("\n\nResult:",sum)

