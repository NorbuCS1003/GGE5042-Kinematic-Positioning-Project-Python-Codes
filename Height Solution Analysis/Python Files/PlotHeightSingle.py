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
    plt.ylabel('Height (m)')
    plt.title('iHeave Value (m)  vs. Epoch for F185')
    plt.legend()
    plt.grid()
    plt.show()


files = [
    'Rover1_Height_Adjusted.txt'
]

labels = ['F185']

plot_data(files, labels)
