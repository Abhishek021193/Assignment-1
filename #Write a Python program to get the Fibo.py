#Write a Python program to get the Fibonacci series between 0 to 50
n1=int(input("enter the first number of range"))
n2=int(input("enter the last number of range"))
print("fibbonacci series between",n1,"to",n2,"is")
x=0
y=1
for i in range(n1,n2):  
    z=x+y
    x=y
    y=z
    print(x, end=" ") 
    if (y>n2):
        break
    