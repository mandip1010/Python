a=eval(input("enter a"))
b=eval(input("enter b"))
c=eval(input("enter c"))

if(a>b and a>c):
    print("a is max")
elif(b>a and b>c):
    print("b is max")
elif(c>a and c>b):
    print("c is max")
elif(a>=b and b>=a):
    print("a and b is max")
elif(b>=c and c>=b):
    print("b and c is max")
else:
    print("a and c is max")