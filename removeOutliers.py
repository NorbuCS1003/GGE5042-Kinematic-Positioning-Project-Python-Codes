import pandas as pd

baseline_file = 'Baseline_Difference_(m).txt'
outlier_file = 'outliers.txt'
cleaned_file = 'Cleaned_Differences.txt'

baseline_data = pd.read_csv(baseline_file, delim_whitespace=True)
outliers_data = pd.read_csv(outlier_file, delim_whitespace=True)

outlier_epochs = set(outliers_data['Epoch'])

cleaned_data = baseline_data[~baseline_data['Epoch'].isin(outlier_epochs)]
cleaned_data.to_csv(cleaned_file, sep='\t', index=False)

print(f"Successful")