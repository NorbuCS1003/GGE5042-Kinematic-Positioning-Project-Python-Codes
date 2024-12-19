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

    # Plot Difference vs Epoch
    plt.figure()
    plt.plot(data['Epoch'], data['Baseline_Difference(m)'], label='Baseline Differences')
    plt.xlabel('Epoch')
    plt.ylabel('Baseline Difference (m)')
    plt.title('Baseline Difference vs Epoch')
    plt.grid()
    plt.show()

    # Plot time series of e
    plt.figure(figsize=(12, 7))
    plt.plot(data['Epoch'], data['e_(m)'])
    plt.ylim(-1, 6)
    plt.xlabel('Epoch')
    plt.ylabel('Differences (m)')
    plt.title('Time Series of Difference e')
    plt.legend()
    plt.grid()
    plt.show()


plot_data('Baseline_Difference_(m).txt')
