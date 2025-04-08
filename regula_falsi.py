import math
log=math.log10
def regula_falsi(f,a,b,tol=1e-6,max_iter=100):
    if f(a)*f(b)>=0:
        print("function values at endoints must have opposite signs")
        return None
    for i in range (max_iter):
        c=a-((b-a)/(f(b)-f(a)))*f(a)
        if abs(f(c))<tol:
            return c
        if f(a)*f(c)<0:
            b=c
        else:
            a=c
    return c
def f(x):
    return x*log(x)-1.2
root=regula_falsi(f,2,3)
if root is not None:
    print ("root found:", root)
