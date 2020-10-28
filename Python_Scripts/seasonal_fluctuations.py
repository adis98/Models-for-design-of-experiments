start = int(input('enter first year\n'))
stop = int(input('enter last year\n'))
gap = int(input('enter the interval btwn years'))

nq = int(input('enter the no of quarters\n'))
no_of_yrs = int(((stop-start)/gap)+1)
data = [0.0]*(no_of_yrs*nq)
totals = [0.0]*nq
avgs = [0.0]*nq
for i in range(0,no_of_yrs):
    for j in range(nq):
        data[nq*i+j] = float(input('enter year'+str(i)+' quarter'+ str(j)+': '))
        totals[j] += data[nq*i+j]
for i in range(nq):
    avgs[i] = totals[i]/no_of_yrs
avg_of_avgs = 0.0
sm = 0.0
sm2 = 0.0
for i in range(nq):
    avg_of_avgs += avgs[i]
    sm2 += totals[i]
sm = avg_of_avgs
avg_of_avgs /= nq

seasonal_indices = [0.0]*nq
for i in range(nq):
    seasonal_indices[i] = (avgs[i]/avg_of_avgs)*100
    
for j in range(no_of_yrs):
    print('{:>15d}'.format(start+gap*j),end = '')
print('{:>15s}{:>15s}{:>15s}'.format('TOTALS','AVGS','SI'))
for i in range(nq):
    for j in range(no_of_yrs):
        print('{:>15.4f}'.format(data[j*nq+i]),end = '')
    print('{:15.4f}{:>15.4f}{:>15.4f}'.format(totals[i],avgs[i],seasonal_indices[i]))
for j in range(no_of_yrs):
    print('{:>15s}'.format(''),end = '')
print('{:>15.4f}{:>15.4f}{:>15s}'.format(sm2,avg_of_avgs,''))
    
