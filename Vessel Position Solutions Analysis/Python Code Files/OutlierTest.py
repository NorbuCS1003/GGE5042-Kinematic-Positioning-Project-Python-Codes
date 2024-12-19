import pandas as pd
import numpy as np


def load_data(file_path):
    # Load the data into a pandas DataFrame
    data = pd.read_csv(file_path, delim_whitespace=True)

    # Ensure the file has the required columns
    required_columns = ['Epoch', 'Baseline_Difference(m)', 'e_(m)']
    for column in required_columns:
        if column not in data.columns:
            raise ValueError(f"Missing required column: {column}")

    epoch = data['Epoch'].to_numpy()
    d = data['Baseline_Difference(m)'].to_numpy()
    e = data['e_(m)'].to_numpy()

    return {
        'epoch': epoch,
        'd': d,
        'e': e
    }


def outlier_test(data, confidence_level=0.95):
    d = data['d']
    e = data['e']
    n = len(d)

    # mean and std calculation
    mu = np.mean(d)
    std = np.std(d, ddof=1)

    # t-statistic for the given confidence level
    t_val = 1.96

    lower_bound = mu - std * t_val
    upper_bound = mu + std * t_val

    outliers = []
    for i, value in enumerate(d):
        if value < lower_bound or value > upper_bound:
            outliers.append((data['epoch'][i], value))

    return {
        'mean': mu,
        'std': std,
        'lower': lower_bound,
        'upper': upper_bound,
        'outliers': outliers
    }


data = load_data('Baseline_Difference_(m).txt')

results = outlier_test(data)

outlier_df = np.array(results['outliers'])

with open('Outliers.txt', 'w') as output:
    output.write('Epoch   Outliers\n')
    np.savetxt(output, outlier_df, fmt='%8.0f %15.3f')

print(f"Mean: {results['mean']}m")
print(f"Standard Deviation: {results['std']}m")
print(f"Lower Bound: {results['lower']}m")
print(f"Upper Bound: {results['upper']}m")
