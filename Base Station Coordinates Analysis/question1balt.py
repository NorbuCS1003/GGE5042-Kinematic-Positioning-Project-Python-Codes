import numpy as np
import pandas as pd


def dms_to_deg(deg, min_, sec):
    # Convert to absolute decimal value
    abs_dec = abs(deg) + (min_ / 60.0) + (sec / 3600.0)
    return -abs_dec if deg < 0 else abs_dec


def deg_to_dms(decimal_degrees):
    sign = -1 if decimal_degrees < 0 else 1
    decimal_degrees = abs(decimal_degrees)

    # Extract the degrees
    degrees = int(decimal_degrees)
    minutes_decimal = (decimal_degrees - degrees) * 60
    minutes = int(minutes_decimal)
    seconds = (minutes_decimal - minutes) * 60

    degrees = degrees * sign

    print(f"{degrees}° {minutes}' {seconds:.5f}\"", end="")


def load_txt_data(file_path):
    column_names = [
        "col0", "col1",
        "lat_deg", "lat_min", "lat_sec",
        "lon_deg", "lon_min", "lon_sec",
        "height", "Q", "ns",
        "sdn", "sde", "sdu",
        "sdne", "sdeu", "sdue",
        "age", "ratio"
    ]

    # Load the CSV File
    df = pd.read_csv(file_path, delim_whitespace=True, comment="%", names=column_names)

    # Convert Latitude and Longitude from DMS to decimal degree
    df['latitude'] = df.apply(lambda row: dms_to_deg(row['lat_deg'], row['lat_min'], row['lat_sec']), axis=1)
    df['longitude'] = df.apply(lambda row: dms_to_deg(row['lon_deg'], row['lon_min'], row['lon_sec']), axis=1)

    # Extract specific columns into lists
    latitude = df['latitude'].to_numpy()
    longitude = df['longitude'].to_numpy()
    height = df['height'].to_numpy()

    # Return the extracted data as a dictionary of lists
    return {
        'latitude': latitude,
        'longitude': longitude,
        'height': height,
    }


def compute_MN(lat_deg, a, e_2):
    lat_rad = np.radians(lat_deg)
    avg_lat = np.mean(lat_rad)
    sin_lat = np.sin(avg_lat)

    M = (a * (1 - e_2)) / ((1 - e_2 * sin_lat ** 2) ** (3 / 2))
    N = a / np.sqrt(1 - e_2 * sin_lat ** 2)

    return M, N


def compute_std(data, M, N):
    # Compute angular differences for latitude and longitude
    dphi = np.radians(data['latitude']) - np.radians(np.mean(data['latitude']))
    dlamb = np.radians(data['longitude']) - np.radians(np.mean(data['longitude']))

    # Convert angular differences to meters
    dphi_m = M * dphi
    dlamb_m = N * np.cos(np.mean(np.radians(data['latitude']))) * dlamb

    # Compute standard deviations
    lat_std = np.std(dphi_m, ddof=1)
    long_std = np.std(dlamb_m, ddof=1)
    H_std = np.std(data['height'], ddof=1)

    return lat_std, long_std, H_std


# GRS80 Parameters
a = 6378137
f = 1 / 298.257222101
e_2 = 2 * f - f ** 2

# Load Data
ppp_data = load_txt_data("Base_ppp_pos.txt")
rel_data = load_txt_data("Base_relative_pos.txt")

# M and N
M_ppp, N_ppp = compute_MN(ppp_data['latitude'], a, e_2)
M_rel, N_rel = compute_MN(rel_data['latitude'], a, e_2)

# Computation
ppp_lat_std, ppp_long_std, ppp_H_std = compute_std(ppp_data, M_ppp, N_ppp)
rel_lat_std, rel_long_std, rel_H_std = compute_std(rel_data, M_rel, N_rel)

print("\n*********** For PPP Static Solution ***********")
print("Latitude: ", end="")
deg_to_dms(np.mean(ppp_data['latitude']))
print(f"        lat_std: {ppp_lat_std}m")
print("Longitude: ", end="")
deg_to_dms(np.mean(ppp_data['longitude']))
print(f"     long_std: {ppp_long_std}m")
print(f"Height: {np.mean(ppp_data['height'])}m        H_std: {ppp_H_std}m")

print("\n*********** For Relative Static Solution ***********")
print("Latitude: ", end="")
deg_to_dms(np.mean(rel_data['latitude']))
print(f"        lat_std: {rel_lat_std}m")
print("Longitude: ", end="")
deg_to_dms(np.mean(rel_data['longitude']))
print(f"     long_std: {rel_long_std}m")
print(f"Height: {np.mean(rel_data['height'])}m        H_std: {rel_H_std}m")
