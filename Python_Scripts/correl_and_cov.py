import numpy as np
m = int(input('enter the number of inputs per variable'))
n = int(input('enter the number of variables'))


table = np.zeros((m,n))



for i in range(m):
    for j in range(n):
        table[i][j] = float(input(':'))
mean_vec = np.sum(table,axis = 0)/m

modif_tab = table-mean_vec

cov_mat = (modif_tab.T).dot(modif_tab)
cov_mat /=(m-1)

print(cov_mat)
