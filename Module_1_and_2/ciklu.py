num = int(input("Enter integer (0 for output): "))
sum = 0
while not num==0:
    for i in range(1,num+1):
        sum=i+sum
    num = int(input("Enter integer (0 for output): "))

print(sum)