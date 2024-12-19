import numpy as np

temp1 = np.loadtxt('Rover2_SPS.pos')

epoch1 = temp1[:, 1]
height = temp1[:, 8]

height_array = np.column_stack((epoch1, height))

with open('Rover2_SPS_Heght_Epoch.txt', 'w') as fout:
    fout.write('Epoch    Height\n')
    np.savetxt(fout, height_array, fmt='%8.0f %15.3f')
