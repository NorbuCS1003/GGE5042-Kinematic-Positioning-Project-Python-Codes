import matplotlib.pyplot as plt
import pandas as pd


def plot_data(files, labels):
    plt.figure(figsize=(12, 8))

    for file_path, label in zip(files, labels):
        data = pd.read_csv(file_path, delim_whitespace=True)

        if 'Epoch' not in data.columns or 'Height' not in data.columns:
            raise ValueError(f"File {file_path} must have 'Epoch' and 'Height' columns")

        plt.plot(data['Epoch'], data['Height'], label=label)

    plt.xlabel('Epoch')
    plt.ylabel('WGS Ellipsoidal Height (m)')
    plt.title('Difference in Height (Rover1 - Rover2) vs. Epoch for Different Processing Methods')
    plt.legend()
    plt.grid()
    plt.show()


files = [
    'SPS_diff.txt',
    'PPP_diff.txt',
    'PPK_diff.txt',
    'NRCan_diff.txt'
]

labels = ['SPS', 'PPP', 'PPK', 'NRCan_PPP']

plot_data(files, labels)
