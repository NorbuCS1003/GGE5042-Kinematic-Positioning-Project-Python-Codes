import numpy as np
import pandas as pd


def load_txt_data(file_path):
    column_names = [
        "col0", "col1",
        'latitude',
        'Longitude',
        "height", "Q", "ns",
        "sdn", "sde", "sdu",
        "sdne", "sdeu", "sdue",
        "age", "ratio"
    ]

    # Load the CSV File
    df = pd.read_csv(file_path, delim_whitespace=True, names=column_names)

    # Extract specific columns into lists
    latitude = df.get('latitude', pd.Series()).to_numpy()
    longitude = df.get('longitude', pd.Series()).to_numpy()
    height = df.get('height', pd.Series()).to_numpy()

    # Return the extracted data as a dictionary of lists
    return {
        'latitude': latitude,
        'longitude': longitude,
        'height': height,
    }


def calculate_velocity(data, file_path):
    a = 6378137.0
    f = 1 / 298.257222101
    e_2 = 2 * f - f ** 2
    phi = np.radians(np.mean(data['latitude']))
    sin_2 = np.sin(phi) ** 2

    # M and N
    M = (a * (1 - e_2)) / ((1 - e_2 * sin_2) ** (3 / 2))
    N = a / (np.sqrt(1 - e_2 * sin_2))

    temp1 = np.loadtxt(file_path)
    epoch = temp1[:, 1]
    laitude = temp1[:, 2]
    longitude = temp1[:, 3]
    height = temp1[:, 4]

    lat_rad = np.radians(laitude)
    long_rad = np.radians(longitude)

    delta_t = np.diff(epoch)
    delta_lat = M * np.diff(lat_rad)
    delta_long = N * np.cos(phi) * np.diff(long_rad)
    delta_height = np.diff(height)

    v_north = delta_lat / delta_t
    v_east = delta_long / delta_t
    v_up = delta_height / delta_t
    epoch_up = epoch[1: ]

    velocity = np.vstack((epoch_up, v_north, v_east, v_up)).T

    return velocity


rov1 = load_txt_data('Rover1_PPK_Deg.pos')
rov2 = load_txt_data('Rover2_PPK_DEG.pos')

velocity_1 = calculate_velocity(rov1, 'Rover1_PPK_Deg.pos')
velocity_2 = calculate_velocity(rov2, 'Rover2_PPK_DEG.pos')

with open('Velocity_Rover1.txt', 'w') as fout:
    fout.write('Epoch   v_north   v_east   v_up\n')
    np.savetxt(fout, velocity_1, fmt='%8.0f %15.3f %15.3f %15.3f')

with open('Velocity_Rover2.txt', 'w') as fout:
    fout.write('Epoch   v_north   v_east   v_up\n')
    np.savetxt(fout, velocity_2, fmt='%8.0f %15.3f %15.3f %15.3f')