import numpy as np

b = int(input('enter the number of blocks'))
v = int(input('enter the number of treatments'))

table = np.zeros((v,b))
miss_row = int(input('enter the missing row_no'))
miss_col = int(input('enter the missng col_no'))

print('enter table values row-wise (assuming treatments are placed one below the other')

for i in range(v):
    for j in range(b):
        table[i][j] = float(input(':'))

table[miss_row-1][miss_col-1] = 0 # just to ensure that its zeroed out

S = np.sum(table)
temp = np.sum(table,axis = 1)
Yt = temp[miss_row-1]
temp2 = np.sum(table,axis=0)
Yb = temp2[miss_col-1]

print('total_sum: ',S,'Treat_tot: ',temp,'Block_tot: ',temp2)

x = (v*Yt + b*Yb -S)/((b-1)*(v-1))

print('X: ',x)
table[miss_row-1][miss_col-1] = x


