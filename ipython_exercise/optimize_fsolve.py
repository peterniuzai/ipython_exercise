from scipy.optimize import fsolve
from math import sin

def f(x):
    x0,x1,x2 = x.tolist()
    return [
        5*x1+3,
        4*x0*x0 - 2*sin(x1*x2),
        x1*x2 - 1.5
             ]

result = fsolve(f, [1,1,1])
print result
print f(result)
