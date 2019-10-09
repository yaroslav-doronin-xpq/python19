import math
def f(x:float):
    c:float
    c=math.asin(x)/(x+1)**2
    return c
def integral (a:float,b:float,n:int):
    h:float
    s:float
    i:int
    h=(b-a)/n
    s=(f(a)+f(b))/2
    i=0
    while(n>i):
        i+=1
        s=s+f(a+h*i)
    return s*h
i:float
a:float
b:float
n:int
n=100

i=integral(0,1,n)
print(i)
