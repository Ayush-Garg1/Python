# 0 1 1 2 3 5 8 13 21 34 ....

# FIBONACCI SEQUENCE

n = int(input("Enter the number : "))

a,b = 0,1
print(a,end = " ")
print(b,end = " ")
for i in range(0,n,1):
    sum = a+b
    print(sum, end = " ")
    a = b
    b = sum