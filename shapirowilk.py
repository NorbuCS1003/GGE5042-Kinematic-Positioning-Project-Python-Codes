import pandas as pd
from scipy.stats import shapiro, kstest

# File paths
baseline_file = "Baseline_Difference_(m).txt"
outliers_file = "outliers.txt"

# Load data
baseline_data = pd.read_csv(baseline_file, delim_whitespace=True)
outliers_data = pd.read_csv(outliers_file, delim_whitespace=True)

# Identify outliers
outlier_epochs = set(outliers_data["Epoch"])

# Remove outliers
cleaned_data = baseline_data[~baseline_data["Epoch"].isin(outlier_epochs)]

# Perform Shapiro-Wilk test on 'Baseline_Difference(m)' column
stat, p_value = shapiro(cleaned_data["Baseline_Difference(m)"])
ks_stat, ks_p_value = kstest(cleaned_data["Baseline_Difference(m)"], 'norm', args=(
    cleaned_data["Baseline_Difference(m)"].mean(), cleaned_data["Baseline_Difference(m)"].std()))

# Output the result
print(f"\n*************** Shapiro-Wilk Test *****************")
print(f"Test Statistics: {stat:.4f}")
print(f"P Value: {p_value:.4f}")
print(f"\n*************** Kolmogorov-Smirnov Test *****************")
print(f"Test Statistics: {ks_stat:.4f}")
print(f"P Value: {ks_p_value:.4f}")