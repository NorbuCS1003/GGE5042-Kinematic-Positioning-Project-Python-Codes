import numpy as np


def dms_to_deg(degrees, minute, seconds):
    dd = abs(degrees) + (minute / 60.0) + (seconds / 3600.0)
    if degrees < 0:
        dd = -dd

    return dd


# GRS80 Parameters
a = 6378137
f = 1 / 298.257222101
e_2 = 2 * f - f ** 2

# Coordinates And Stdev
# PPP
ppp_lat = dms_to_deg(45, 57, 00.98711)
ppp_long = dms_to_deg(-66, 38, 32.25614)
ppp_H = 19.5689
ppp_lat_std = 0.0037
ppp_long_std = 0.006
ppp_H_std = 0.0073

# Relative
rel_lat = dms_to_deg(45, 57, 00.98869)
rel_long = dms_to_deg(-66, 38, 32.23789)
rel_H = 19.2174
rel_lat_std = 0.0036
rel_long_std = 0.0061
rel_H_std = 0.0087

print(rel_lat, rel_long)

# Avg Stds
lat_std = np.sqrt(ppp_lat_std ** 2 + rel_lat_std ** 2)
long_std = np.sqrt(ppp_long_std ** 2 + rel_long_std ** 2)
H_std = np.sqrt(ppp_H_std ** 2 + rel_H_std ** 2)

# M and N
ave_phi = (ppp_lat+rel_lat)/2
M = (a * (1 - e_2)) / (1 - (e_2 * (np.sin(np.radians(ave_phi))) ** 2)) ** (3 / 2)
N = a / np.sqrt(1 - (e_2 * (np.sin(np.radians(ave_phi)))**2))

# delta Values
delta_lat = M * abs(ppp_lat - rel_lat)
delta_long = N * np.cos(np.radians(ave_phi)) * abs(ppp_long-rel_long)
delta_H = abs(ppp_H-rel_H)

# Test
ef = 1.96

to_test = [
    ("Latitude", delta_lat, lat_std),
    ("Longitude", delta_long, long_std),
    ("Height", delta_H, H_std)
]

for label, delta_val, std_val in to_test:
    if delta_val <= (ef * std_val):
        print(f"The final {label} are statistically equivalent at 95% Confidence Level")
    else:
        print(f"For {label}:")
        print(f"{delta_val} ≤ {ef * std_val}")
        print(f"The Test Failed!\n")


