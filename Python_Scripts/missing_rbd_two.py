import numpy as np

b = int(input('enter the number of blocks'))
v = int(input('enter the number of treatments'))

table = np.zeros((v,b))
mtx = int(input('enter the missing row_no_x'))
mbx = int(input('enter the missng col_no_x'))
mty = int(input('enter the missing row_no_y'))
mby = int(input('enter the missng col_no_y'))

print('enter table values row-wise (assuming treatments are placed one below the other')

for i in range(v):
    for j in range(b):
        table[i][j] = float(input(':'))

table[mtx-1][mbx-1] = 0 # just to ensure that its zeroed out
table[mty-1][mby-1]= 0

S = np.sum(table)

rtx=0
rbx=0
rty=0
rby=0
for i in range(b):
    rtx += table[mtx-1][i]
    rty += table[mty-1][i]

for i in range(v):
    rbx += table[i][mbx-1]
    rby += table[i][mby-1]
print('S :',S,'Rbx: ',rbx,'Rtx: ',rtx,'Rby: ',rby,'Rty: ',rty)
print('eq1: ',(b-1)*(v-1),'X',' = ',b*rbx +v*rtx -S,'-Y')
print('eq2: ',(b-1)*(v-1),'Y',' = ',b*rby + v*rty -S,'-X')
