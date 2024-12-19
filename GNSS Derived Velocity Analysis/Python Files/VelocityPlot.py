import matplotlib.pyplot as plt
import pandas as pd


def plot_data(file_path):
    # Load the data into a pandas DataFrame
    data = pd.read_csv(file_path, delim_whitespace=True)

    # Ensure the file has the required columns
    required_columns = ['Epoch', 'v_north', 'v_east', 'v_up']
    for column in required_columns:
        if column not in data.columns:
            raise ValueError(f"Missing required column: {column}")

    # V_north vs Epoch
    plt.figure(figsize=(12, 5))
    plt.plot(data['Epoch'], data['v_north'], label='V_north')
    plt.xlabel('Epoch')
    plt.ylabel('Velocity (m/s)')
    plt.title('Rover2 - F185, Difference in North Velocity')
    plt.grid()
    plt.show()

    # V_east vs Epoch
    plt.figure(figsize=(12, 5))
    plt.plot(data['Epoch'], data['v_east'], label='V_east')
    plt.xlabel('Epoch')
    plt.ylabel('Velocity (m/s)')
    plt.title('Rover2 - F185, Difference in East Velocity')
    plt.grid()
    plt.show()

    # V_vertical vs Epoch
    plt.figure(figsize=(12, 5))
    plt.plot(data['Epoch'], data['v_up'], label='V_up')
    plt.xlabel('Epoch')
    plt.ylabel('Velocity (m/s)')
    plt.title('Rover2 - F185, Difference in Vertical Velocity')
    plt.grid()
    plt.show()


plot_data('F185_Rover2_Vdiff.txt')
