import matplotlib.pyplot as plt
import pandas as pd


def plot_data(file_path):
    # Load the data into a pandas DataFrame
    data = pd.read_csv(file_path, delim_whitespace=True)

    # Ensure the file has the required columns
    required_columns = ['Epoch', 'Baseline_Difference(m)', 'e_(m)']
    for column in required_columns:
        if column not in data.columns:
            raise ValueError(f"Missing required column: {column}")

    # Plot time series of e
    plt.figure(figsize=(10, 6))
    plt.hist(data['Baseline_Difference(m)'], bins=50, edgecolor='black', alpha=0.7)
    plt.title('Histogram of Baseline Differences without Outliers', fontsize=16)
    plt.xlabel('Baseline Difference (m)', fontsize=14)
    plt.ylabel('Frequency', fontsize=14)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

plot_data('Baseline_Difference_(m).txt')
plot_data('Cleaned_Differences.txt')