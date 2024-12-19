import numpy as np

temp1 = np.loadtxt('Velocity_Rover2.txt', skiprows=1)
temp2 = np.loadtxt('Velocity_F185.txt', skiprows=1)

epoch1 = temp1[:, 0]
epoch2 = temp2[:, 0]
data1 = temp1[:, [1, 2, 3]]
data2 = temp2[:, [1, 2, 3]]

epoch3, ind1, ind2 = np.intersect1d(epoch1, epoch2, return_indices=True)

results = []

for i in range(len(epoch3)):
    diff = data1[ind1[i], :] - data2[ind2[i], :]
    results.append([epoch3[i], diff[0], diff[1], diff[2]])

results_array = np.array(results)

with open('F185_Rover2_Vdiff.txt', 'w') as fout:
    fout.write('Epoch   v_north   v_east   v_up\n')
    np.savetxt(fout, results_array, fmt='%8.0f %15.3f %15.3f %15.3f')

