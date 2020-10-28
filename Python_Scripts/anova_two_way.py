import numpy as np

n_B = int(input('enter the number of blocks'))
n_T = int(input('enter the number of treatments'))

table = np.zeros((n_T,n_B))
for i in range(n_T):
    print('enter values for treatment'+ str(i+1))
    for j in range(n_B):
        table[i][j] = float(input(':'))
global_mean = np.mean(table)
global_total = np.sum(table)
print('global_total:', global_total,'global_mean: ',global_mean)
block_means = np.sum(table,axis = 0)
block_means /= n_T
treat_means = np.sum(table,axis = 1)
print(treat_means)
treat_means /= n_B
block_totals = block_means * n_T
treat_totals = treat_means * n_B
print('block_totals: ',block_totals,'block_means: ',block_means)
print('treatment_totals: ',treat_totals,'treat_means: ',treat_means)

ssb = n_T*np.sum((block_means-global_mean)*(block_means-global_mean))
sst = n_B*(np.sum((treat_means-global_mean)*(treat_means-global_mean)))
ss_total = np.sum((table-global_mean)*(table-global_mean))

print('ss_block: ',ssb,'ss_treats: ',sst,'ss_total: ',ss_total)

mssb = ssb/(n_B-1)
msst = sst/(n_T-1)

sse = ss_total-ssb-sst
msse = sse/(n_B*n_T-n_B-n_T+1)
print('ss_error: ',sse)
print('mss_blocks: ',mssb,'mss_treats: ',msst,'mss_error: ',msse)
f_stat_treats = msst/msse
f_stat_blocks = mssb/msse

print('f_treats_stat: ',f_stat_treats,'f_blocks_stat: ',f_stat_blocks)

