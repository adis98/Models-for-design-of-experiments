import numpy as np
num_fact = int(input('enter the number of factors'))
n_replic = int(input('enter the number of replications'))
borno = int(input('split into blocks?'))

n_rows = int(2**num_fact)
n_cols = n_replic

table = np.zeros((n_rows,n_cols))

for i in range(n_rows):
    print("enter for row" ,i+1)
    for j in range(n_cols):
        table[i][j] = float(input(':'))

totals = np.sum(table,axis = 1)

global_total = np.sum(table)

print('global total is: ',global_total)

print('totals are: ',totals)

cf = (global_total**2)/(n_rows * n_replic)

print('cf: ',cf)

block_totals = 0

if(borno == 1):
    block_totals = np.sum(table,axis = 0)
    print('block_totals: ',block_totals)


SS_blocks = 0
df_blocks = 0
MSS_blocks = 0

if(borno == 1):
    df_blocks = n_replic - 1
    SS_blocks = (np.sum(block_totals * block_totals))/(n_rows) - cf
    MSS_blocks = SS_blocks/(df_blocks)
    print('SS BLOCKS: ',SS_blocks)
    print('MSS BLOCKS: ',MSS_blocks)
    
    

SST = np.sum(table*table) - cf

if (num_fact ==2):
    effects = []
    contrast_A = totals[3]+totals[1]-totals[0]-totals[2]
    A_effect = contrast_A/(2*n_replic)
    SSA = (contrast_A**2)/(n_rows * n_replic)
    contrast_B = totals[3]+totals[2]-totals[0]-totals[1]
    B_effect = contrast_B/(2*n_replic)
    SSB = (contrast_B**2)/(n_rows * n_replic)
    contrast_AB = totals[3]+totals[0]-totals[1]-totals[2]
    AB_effect = contrast_AB/(2*n_replic)
    SSAB = (contrast_AB**2)/(n_rows * n_replic)
    SS_error = SST - SSA - SSB - SSAB - SS_blocks
    SS = []
    SS.append(SSA)
    SS.append(SSB)
    SS.append(SSAB)
    SS.append(SS_error)
    SS.append(SST)
    print('SSA,SSB,SSAB,SSERROR,SSTOTal: ',SS)
    MSS_error = SS_error/(n_rows * n_replic - 4 - df_blocks)
    print('mss_error/df :', MSS_error)
    F_STAT = []
    F_STAT.append(SSA/MSS_error)
    F_STAT.append(SSB/MSS_error)
    F_STAT.append(SSAB/MSS_error)
    print("F_stat a,b,ab: ",F_STAT)
    print('')
    effects.append(A_effect)
    effects.append(B_effect)
    effects.append(AB_effect)
    print('effects: a,b,ab: ',effects)

elif(num_fact ==3):
    effects = []
    contrast_A = totals[3]+totals[1]+totals[5] + totals[7]-totals[0]-totals[2]-totals[4]-totals[6]
    A_effect = contrast_A/(4*n_replic)
    SSA = (contrast_A**2)/(n_rows * n_replic)
    
    contrast_B = totals[3]-totals[1]-totals[5] + totals[7]-totals[0]+totals[2]-totals[4]+totals[6]
    B_effect = contrast_B/(4*n_replic)
    SSB = (contrast_B**2)/(n_rows * n_replic)
    
    contrast_AB = totals[0]+totals[3]+totals[4] + totals[7]-totals[1]-totals[2]-totals[5]-totals[6]
    AB_effect = contrast_AB/(4*n_replic)
    SSAB = (contrast_AB**2)/(n_rows * n_replic)
    
    contrast_C = totals[4]+totals[5]+totals[6] + totals[7]-totals[0]-totals[2]-totals[1]-totals[3]
    C_effect = contrast_C/(4*n_replic)
    SSC = (contrast_C**2)/(n_rows * n_replic)

    contrast_AC = totals[0]+totals[2]+totals[5] + totals[7]-totals[1]-totals[3]-totals[4]-totals[6]
    AC_effect = contrast_AC/(4*n_replic)
    SSAC = (contrast_AC**2)/(n_rows * n_replic)

    contrast_BC = totals[0]+totals[1]+totals[6] + totals[7]-totals[3]-totals[2]-totals[4]-totals[5]
    BC_effect = contrast_BC/(4*n_replic)
    SSBC = (contrast_BC**2)/(n_rows * n_replic)

    contrast_ABC = totals[2]+totals[1]+totals[4] + totals[7]-totals[0]-totals[3]-totals[5]-totals[6]
    ABC_effect = contrast_ABC/(4*n_replic)
    SSABC = (contrast_ABC**2)/(n_rows * n_replic)
    
    
    SS_error = SST - SSA - SSB - SSAB -SSC - SSAC - SSBC - SSABC - SS_blocks
    SS = []
    SS.append(SSA)
    SS.append(SSB)
    SS.append(SSAB)
    SS.append(SSC)
    SS.append(SSAC)
    SS.append(SSBC)
    SS.append(SSABC)
    SS.append(SS_error)
    SS.append(SST)
    print('SSA,SSB,SSAB,,SSC,SSAC,SSBC,SSABC, SSERROR,SSTOTal: ',SS)
    MSS_error = SS_error/(n_rows * n_replic - 8 - df_blocks)
    print('mss_error/df :', MSS_error)
    F_STAT = []
    F_STAT.append(SSA/MSS_error)
    F_STAT.append(SSB/MSS_error)
    F_STAT.append(SSAB/MSS_error)
    F_STAT.append(SSC/MSS_error)
    F_STAT.append(SSAC/MSS_error)
    F_STAT.append(SSBC/MSS_error)
    F_STAT.append(SSABC/MSS_error)
    print("F_stat a,b,ab,c,ac,bc,abc: ",F_STAT)

    print('')
    effects.append(A_effect)
    effects.append(B_effect)
    effects.append(AB_effect)
    effects.append(C_effect)
    effects.append(AC_effect)
    effects.append(BC_effect)
    effects.append(ABC_effect)
    print('effects: a,b,ab,c,ac,bc,abc: ',effects)
    


    
    
    
    



