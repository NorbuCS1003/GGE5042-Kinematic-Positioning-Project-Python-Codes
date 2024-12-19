import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def plot_data(file_path):
    # Load the data into a pandas DataFrame
    data = pd.read_csv(file_path, delim_whitespace=True)

    # Ensure the file has the required columns
    required_columns = ['Epoch', 'Dlat', 'DLon', 'DHoriz', 'Dheight']
    for column in required_columns:
        if column not in data.columns:
            raise ValueError(f"Missing required column: {column}")

    # Plot Dlat vs Epoch
    plt.figure()
    plt.plot(data['Epoch'], data['Dlat'], label='Difference in latitude')
    plt.xlabel('Epoch')
    plt.ylabel('Difference in latitude (metres)')
    plt.title('Difference in latitude vs Epoch')
    plt.legend()
    plt.grid()
    plt.show()

    # Plot DLon vs Epoch
    plt.figure()
    plt.plot(data['Epoch'], data['DLon'], label='Difference in Longitude')
    plt.xlabel('Epoch')
    plt.ylabel('Difference in Longitude (meters)')
    plt.title('Difference in Longitude vs Epoch')
    plt.legend()
    plt.grid()
    plt.show()

    # Plot DHoriz vs Epoch
    plt.figure()
    plt.plot(data['Epoch'], data['DHoriz'], label='Difference in Horizontal Position')
    plt.xlabel('Epoch')
    plt.ylabel('Difference in Horizontal Position (meters)')
    plt.title('Difference in Horizontal Position (d) vs Epoch')
    plt.legend()
    plt.grid()
    plt.show()

    # Plot Dheight vs Epoch
    plt.figure()
    plt.plot(data['Epoch'], data['Dheight'], label='Difference in Height')
    plt.xlabel('Epoch')
    plt.ylabel('Difference in Height (metres)')
    plt.title('Difference in Height vs Epoch')
    plt.legend()
    plt.grid()
    plt.show()


def calculate_std_deviation(file_path):
    # Load the data into a pandas DataFrame
    data = pd.read_csv(file_path, delim_whitespace=True)

    # Filter out rows where Epoch is 500000
    filtered_data = data[data['Epoch'] < 500000]

    # Calculate standard deviations
    stats = {
        'Dlat': {'std': np.std(filtered_data['Dlat'], ddof=1), 'mean': np.mean(filtered_data['Dlat'])},
        'DLon': {'std': np.std(filtered_data['DLon'], ddof=1), 'mean': np.mean(filtered_data['DLon'])},
        'DHoriz': {'std': np.std(filtered_data['DHoriz'], ddof=1), 'mean': np.mean(filtered_data['DHoriz'])},
        'Dheight': {'std': np.std(filtered_data['Dheight'], ddof=1), 'mean': np.mean(filtered_data['Dheight'])}
    }

    return stats


def print_stats(stats):
    for key, value in stats.items():
        print(f"{key}:", end="")
        print(f"  Standard deviation: {value['std']:.3f}", end="")
        print(f"  Mean: {value['mean']:.3f}")


std_devs = calculate_std_deviation('Compare_NRCan_PPK.txt')
print_stats(std_devs)

