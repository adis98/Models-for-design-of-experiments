import numpy as np
no_treat = int(input('enter the number of treatments'))
no_trials = [0]*no_treat
for i in range(no_treat):
    no_trials[i] = int(input('enter the no of trials for treatment'+ str(i+1)))
    
indiv_means = [0.0]*no_treat
mx = max(no_trials)
table = np.zeros((no_treat,mx))
treatment_totals = [0.0]*no_treat
for i in range(no_treat):
    print('enter values for treatment'+str(i+1))
    mean = 0.0
    for j in range(no_trials[i]):
        table[i][j] = float(input(': '))
        mean += table[i][j]
    mean /=no_trials[i]
    indiv_means[i] = mean
    treatment_totals[i] = mean * no_trials[i]
global_mean = np.sum(table)
global_mean /= sum(no_trials)
total_sum = global_mean * sum(no_trials)

ss_treat = 0.0
for i in range(no_treat):
    ss_treat += no_trials[i] * (indiv_means[i]-global_mean)**2

ss_total = 0.0
for i in range(no_treat):
    for j in range(no_trials[i]):
        ss_total += (table[i][j]-global_mean)**2


mss_treat = ss_treat/(no_treat-1)
ss_error = ss_total - ss_treat
mss_error = ss_error/(sum(no_trials) - no_treat)
f_stat = mss_treat/mss_error
print("global_mean: ",global_mean,"sum_total: ", total_sum)
print('treatment_means:', indiv_means)
print('treatment_totals: ' , treatment_totals)
print('ss_treat: ',ss_treat,'ss_error: ',ss_error)
print('mss_treat: ',mss_treat,'mss_error: ',mss_error)
print('f_stat: ',f_stat)
