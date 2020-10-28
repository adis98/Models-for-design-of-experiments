y1 = int(input("enter the starting year "))
y2 = int(input("enter the ending year "))
diff = int(input("enter the difference between years "))
no_of_eles = int((y2-y1)/diff + 1)
years = []
eles = []
for i in range(no_of_eles):
    temp = y1+i*diff
    temp1 = float(input("enter the value for "+str(temp)+" "))
    years.append(temp)
    eles.append(temp1)
t = [] # t holds the modified years

if (no_of_eles%2 == 1):#odd no of values
    middle_index = int(no_of_eles/2)
    t.append(-middle_index)
    for i in range(1,no_of_eles):
        t.append(t[i-1]+1)
elif (no_of_eles%2 == 0):#even no of values
    middle_index = int(no_of_eles/2)
    t.append(1-2*middle_index)
    for i in range(1,no_of_eles):
        t.append(t[i-1]+2)
tp = []
for i in range(no_of_eles):
    tp.append(t[i]*eles[i])
sigma_t = 0
sigma_t_sq = 0
sigma_tp = 0
sigma_p = 0
for i in range(no_of_eles):
    sigma_t = sigma_t + t[i]
    sigma_t_sq = sigma_t_sq + t[i]*t[i]
    sigma_tp = sigma_tp + tp[i]
    sigma_p = sigma_p + eles[i]
#if regression is of the form at + b
a = sigma_tp/sigma_t_sq
b = sigma_p/no_of_eles
print("a = %.4f b = %.4f"%(a,b))
print("")
p_pred = []
for i in range(no_of_eles):
    p_pred.append(a*t[i]+b)

#for eliminating trend
diff_trend = []
mul_trend = []
for i in range(no_of_eles):
    diff_trend.append(eles[i]-p_pred[i])
    mul_trend.append(eles[i]/p_pred[i])


print('{:>8s}{:>15.4s}{:>15.4s}{:>15.5s}{:>15.4s}{:>15.4s}'.format('YEAR','VAL','T','TxVAL','T^2','PRED'))
for i in range(no_of_eles):
    print('{:>8d}{:>15.4f}{:>15.4f}{:>15.4f}{:>15.4f}{:>15.4f}'.format(years[i],eles[i],t[i],tp[i],t[i]**2,p_pred[i]))
print('{:>8s}{:>15.4f}{:>15.4f}{:>15.4f}{:>15.4f}{:>15.4s}'.format('TOTALS',sigma_p,sigma_t,sigma_tp,sigma_t_sq,''))

print("")
print('{:>8s}{:>15s}{:>15s}'.format('YEAR','ADD TREND','MUL TREND'))
for i in range(no_of_eles):
    print('{:>8d}{:>15.4f}{:>15.4f}'.format(years[i],diff_trend[i],mul_trend[i]))
    


    
