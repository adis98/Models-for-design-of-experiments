import math
lambd = float(input('enter the value of lambda'))
t = float(input('enter the time interval t'))
t1 = int(input('enter lower bound for poisson sum'))
t2 = int(input('enter upper bound for poisson sum'))
sm = 0.0
r = lambd*t
for i in range(t1,t2):
    sm += (rate**i)*(math.exp(-rate))/math.fact(i)
print('sigma val: ',sm)
