import pandas as pd


rover1_data = pd.read_csv('Rover1_PPK_Heght_Epoch.txt', delim_whitespace=True, names=['Epoch', 'Height'], skiprows=1)
f185_data = pd.read_csv('F185_Height.txt', delim_whitespace=True, names=['Epoch', 'Height'], skiprows=1)

up_offset = 0.432 # meters


merged_data = pd.merge(rover1_data, f185_data, on='Epoch', suffixes=('_Rover1', '_F185'))

# Compute the difference and apply the up offset
merged_data['Height_with_Offset'] = ((merged_data['Height_Rover1'] - merged_data['Height_F185']) - up_offset).round(4)
output_data = merged_data[['Epoch', 'Height_with_Offset']]

# Save the results to a new file
output_file = 'Rover1_Height_Adjusted.txt'
output_data.to_csv(output_file, index=False, sep='\t', header=['Epoch', 'Height'])

print(f"Height differences with up offset applied saved to {output_file}")
