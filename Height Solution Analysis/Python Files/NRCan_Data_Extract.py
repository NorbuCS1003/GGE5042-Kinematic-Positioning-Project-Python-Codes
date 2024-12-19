import numpy as np

temp1 = np.loadtxt('Compare_NRCAN.txt', skiprows=1)
temp2 = np.loadtxt('Rover2.csv', delimiter=',', skiprows=1)

epoch = temp1[:, 0]
height = temp2[:, 2]

min_length = min(len(epoch), len(height))
epoch = epoch[:min_length]
height = height[:min_length]

height_array = np.column_stack((epoch, height))

with open('Rover2_NRCan_Heght_Epoch.txt', 'w') as fout:
    fout.write('Epoch    Height\n')
    np.savetxt(fout, height_array, fmt='%8.0f %15.3f')
