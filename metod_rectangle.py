import math
def f(x:float):
    c:float
    c=math.asin(x)/(x+1)**2
    return c

def rectangular(f, a, b, n):
	h = float(b - a)/n
	result = f(a+0.5*h)
	for i in range(1, n):
		result += f(a + 0.5*h + i*h)
	result *= h
	return result
a=0
b=1
for i in range(1, 21):
	n = 2**i
	r = rectangular(f, a, b, n)
	print(r)
