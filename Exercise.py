#question 1
a = int(input("enter a number:"))
b = int(input("enter the limit number:"))

for i in range(1,b+1):
    c = a*i
    print(a,"x",i,"=",c)

x = 1
while x<=b:
    f=x*a
    print(a,"x",x,"=",f)
    x+=1

#question 2
w = 1
while w<=10:
    print(w*" *")
    w+=1

for i in range(1,10):
    print(i *"x ")

z=10
while z>=1:
    print(z *"$ ")
    z-=1

#question 3
for i in range(1,10):
    if i==3:
        continue
    if i==7:
        break
    print("outer loop:", i)
    for j in range(1,4):
        if j==3:
            continue
        print("inner loop:", j)