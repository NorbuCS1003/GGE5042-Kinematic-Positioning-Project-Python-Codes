import pandas as pd
import numpy as np


def load_data(file_path):
    # Load the data into a pandas DataFrame
    data = pd.read_csv(file_path, delim_whitespace=True)

    # Ensure the file has the required columns
    required_columns = ['Epoch', 'v_north', 'v_east', 'v_up']
    for column in required_columns:
        if column not in data.columns:
            raise ValueError(f"Missing required column: {column}")

    epoch = data['Epoch'].to_numpy()
    v_north = data['v_north'].to_numpy()
    v_east = data['v_east'].to_numpy()
    v_up = data['v_up'].to_numpy()

    return {
        'epoch': epoch,
        'v_north': v_north,
        'v_east': v_east,
        'v_up': v_up
    }


def calculate_stat(data):
    v_n = data['v_north']
    v_e = data['v_east']
    v_u = data['v_up']

    mu_vn = np.mean(v_n)
    mu_ve = np.mean(v_e)
    mu_vu = np.mean(v_u)

    std_vn = np.std(v_n, ddof=1)
    std_ve = np.std(v_e, ddof=1)
    std_vu = np.std(v_u, ddof=1)

    return {
        'vn': mu_vn,
        've': mu_ve,
        'vu': mu_vu,
        's_vn': std_vn,
        's_ve': std_ve,
        's_vu': std_vu
    }


data = load_data('F185_Rover1_Vdiff.txt')

results = calculate_stat(data)

print(f"Mean Vn: {results['vn']:.4f}")
print(f"Mean Ve: {results['ve']:.4f}")
print(f"Mean Vu: {results['vu']:.4f}")

print(f"Std Vn: {results['s_vn']:.4f}")
print(f"Std Ve: {results['s_ve']:.4f}")
print(f"Std Vu: {results['s_vu']:.4f}")
