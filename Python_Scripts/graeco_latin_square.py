import numpy as np
n = int(input('enter the number of treatments'))

latin_square = np.zeros((n,n))
for i in range(n):
    print('enter values for row'+str(i+1))
    for j in range(n):
        latin_square[i][j] = float(input(':'))
treats = np.zeros((n,n))
greek = np.zeros((n,n))
for i in range(n):
    print('enter row-wise locations for treatment' + str(i+1))
    for j in range(n):
        loc = int(input(':'))
        treats[i][j] = latin_square[j][loc-1]

for i in range(n):
    print('enter row-wise locations for greeks' + str(i+1))
    for j in range(n):
        loc = int(input(':'))
        greek[i][j] = latin_square[j][loc-1]

total_treats = np.sum(treats,axis = 1)
total_greek = np.sum(greek,axis=1)
total_rows = np.sum(latin_square,axis = 1)
total_cols = np.sum(latin_square,axis = 0)

total_sum = np.sum(latin_square)

global_mean = np.mean(latin_square)

print('tot_rows: ',total_rows,'tot_cols: ',total_cols,'tot_treats: ',total_treats,'total_greek: ',total_greek)
print('global_total: ',total_sum,'global_mean: ',global_mean)

ss_total = np.sum((latin_square - global_mean)*(latin_square - global_mean))
ss_treats = np.sum(total_treats * total_treats)/n - (total_sum**2)/(n*n)
ss_greek = np.sum(total_greek * total_greek)/n - (total_sum**2)/(n*n)
ss_rows = np.sum(total_rows * total_rows)/n - (total_sum**2)/(n*n)
ss_cols = np.sum(total_cols * total_cols)/n - (total_sum**2)/(n*n)
ss_error = ss_total - ss_treats - ss_cols - ss_rows - ss_greek
print('ss_total: ', ss_total,'ss_rows: ',ss_rows,'ss_cols: ',ss_cols,'ss_treats: ',ss_treats,'ss_greek: ',ss_greek,'ss_error: ',ss_error)
mss_treats = ss_treats/(n-1)
mss_greek = ss_greek/(n-1)
mss_cols = ss_cols/(n-1)
mss_rows = ss_rows/(n-1)
mss_error = ss_error/((n-3)*(n-1))

print('mss_treats: ',mss_treats,'mss_cols: ',mss_cols,'mss_rows: ',mss_rows,'mss_greek: ',mss_greek,'mss_error: ',mss_error)
f_stat_treats = mss_treats/mss_error
f_stat_cols = mss_cols/mss_error
f_stat_rows = mss_rows/mss_error
f_stat_greek = mss_greek/mss_error

print('f_treats: ',f_stat_treats,'f_cols: ',f_stat_cols,'f_rows: ',f_stat_rows,'f_greek: ',f_stat_greek)




