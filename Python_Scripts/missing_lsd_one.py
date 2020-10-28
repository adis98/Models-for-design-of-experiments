import numpy as np

n = int(input('enter the number of treatments'))


table = np.zeros((n,n))
miss_row = int(input('enter the missing row_no'))
miss_col = int(input('enter the missng col_no'))

print('enter table values row-wise (assuming treatments are placed one below the other')

for i in range(n):
    for j in range(n):
        table[i][j] = float(input(':'))

table[miss_row-1][miss_col-1] = 0 # just to ensure that its zeroed out

print('enter the columns for the missing treatment element row-wise')

total_treats = 0
for i in range(n):
    col = int(input(':'))
    total_treats += table[i][col-1]
    
S = np.sum(table)
temp = np.sum(table,axis = 1)
Yt = temp[miss_row-1]
temp2 = np.sum(table,axis=0)
Yb = temp2[miss_col-1]

print('total_sum: ',S,'Treat_tot: ',total_treats,'col_tot: ',Yb,'row_total: ',Yt)

x = (n*(Yb+Yt+total_treats) - 2*S)/((n-1)*(n-2))

print('X: ',x)
table[miss_row-1][miss_col-1] = x
