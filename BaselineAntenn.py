import numpy as np


def calculate_d(lat1, lon1, lat2, lon2, h1, h2):
    a = 6378137.0
    f = 1 / 298.257222101
    e_2 = 2 * f - f ** 2
    phi = np.deg2rad(lat1)

    # M and N Calculation
    M = (a * (1 - e_2)) / ((1 - e_2 * (np.sin(phi)) ** 2) ** (3 / 2))
    N = a / (np.sqrt(1 - e_2 * (np.sin(phi)) ** 2))

    # Difference in lat and long
    dlat = M * np.deg2rad(lat1 - lat2)
    dlon = N * np.cos(phi) * np.deg2rad(lon1 - lon2)

    # Difference in height
    dh = h1 - h2
    d = np.sqrt(dlat ** 2 + dlon ** 2 + dh ** 2)
    return d


temp1 = np.loadtxt('Rover1_PPK_Deg.txt')
temp2 = np.loadtxt('Rover2_PPK_DEG.txt')

epoch1 = temp1[:, 1]
epoch2 = temp2[:, 1]
data1 = temp1[:, [2, 3, 4]]
data2 = temp2[:, [2, 3, 4]]

epoch3, ind1, ind2 = np.intersect1d(epoch1, epoch2, return_indices=True)

results = []

for i in range(len(epoch3)):
    lat1, lon1, height1 = data1[ind1[i], :]
    lat2, lon2, height2 = data2[ind2[i], :]

    horizontal_distance = calculate_d(lat1, lon1, lat2, lon2, height1, height2)

    e = horizontal_distance - 0.868

    results.append([epoch3[i], horizontal_distance, e])

results_array = np.array(results)
print(results_array)

with open('Baseline_Difference_(m).txt', 'w') as output:
    output.write('Epoch   Baseline_Difference(m)   e_(m)\n')
    np.savetxt(output, results_array, fmt='%8.0f %15.3f %15.3f')

print("Successfully computed to Baseline_Difference_(m).txt")
