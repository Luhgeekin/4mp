import numpy as np 
from scipy import optimize 
from scipy.misc import derivative 
import math 

x0 = 0.5
y0 = 1.7
delta = 0.1 

def f1(y): 
    return 1.3 - math.sin(y - 1)

def f2 (x): 
    return 0.8 + math.sin(x + 1)

def iter (x,y,e): 
    xn = x 
    yn = y 
    xn1 = f2(x) 
    yn1 = f1(y) 
    n = 1 

    while ((abs(xn1-xn)>=e) & (abs(yn1-yn) >=e)): 
        xn = xn1 
        yn = yn1 
        xn1 = f2(yn) 
        yn1 = f1(xn) 
        n += 1 

    print ('Simple iteration:') 

    print ('x=', xn, '\ny=',yn,'\nThe amount of iteration = ',n) 

iter(x0,y0,0.0001) 

def f3(x):
    eq1 = np.sin(x[1] - 1) + x[0] - 1.3
    eq2 = x[1] - np.sin(x[0] + 1) - 0.8
    return [eq1, eq2]

s = optimize.root(f3, [0.,0.], method = 'hybr')

print ('Chek',s.x) 