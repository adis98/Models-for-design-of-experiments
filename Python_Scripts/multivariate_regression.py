import numpy as np
rx = int(input('enter the no of rows of inputs'))
cx = int(input('enter the no of cols of inputs'))

ry = int(input('enter the no of rows of output'))
cy = int(input('enter the no of cols of output'))

X = np.zeros((rx,cx+1))
Y = np.zeros((ry,cy))
print('enter X')
for i in range(rx):
    for j in range(cx+1):
        if (j==0):
            X[i][j] = 1
        else:
            X[i][j] = float(input(':'))

print('enter Y')
for i in range(ry):
    for j in range(cy):
        Y[i][j] = float(input(':'))
        
B = np.linalg.inv((X.T).dot(X)).dot((X.T).dot(Y))

print('B',B)

int c = int(intput('continue 0/1'))

if( c != 0):
    Yt = Y.T
    Y_cap = (np.mean(Y,axis = 0)).T
    y_capt = y_cap.T
    Xt = X.T
    Bt = B.T
    E = Yt.dot(Y) - (Bt.dot(Xt)).dot(Y)
    print('E: ',E)
    H = (Bt.dot(Xt)).dot(Y) - rx * Y_cap.dot(Y_capt)


