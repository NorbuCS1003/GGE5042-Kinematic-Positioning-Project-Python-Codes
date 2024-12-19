import pandas as pd
from datetime import datetime, timedelta


def convert_to_gpst_seconds(date, time):
    try:
        # Combine date and time, and parse as datetime object
        utc_minus_3 = datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M:%S.%f")
        # Convert to UTC by adding 3 hours
        utc_time = utc_minus_3 + timedelta(hours=3)
        # Convert to GPST by adding 18 seconds
        gpst_time = utc_time + timedelta(seconds=18)
        # GPS epoch (start of GPS time)
        gps_epoch = datetime(1980, 1, 6, 0, 0, 0)
        # Calculate seconds since GPS epoch
        total_seconds = int((gpst_time - gps_epoch).total_seconds())
        # Calculate seconds within the current GPS week
        gpst_week_seconds = total_seconds % (7 * 24 * 60 * 60)
        return gpst_week_seconds

    except Exception:
        return None


path = 'Oct4_KinPositioning_F180_processed_1Hz.csv'
data_df = pd.read_csv(path)

#data_df['iHeave Value (m)'] = pd.to_numeric(data_df['iHeave Value (m)'], errors='coerce')
#data_df = data_df.dropna(subset=['iHeave Value (m)'])

data_df['GPST_Seconds'] = data_df.apply(
    lambda x: convert_to_gpst_seconds(x['Date'], x['Time(UTC-3)']), axis=1)

gpst_seconds_lat_lon_height_df = data_df[['GPST_Seconds', 'Roll']]

# Save to a new CSV file
output_csv_path = "F185_Roll.txt"
gpst_seconds_lat_lon_height_df.to_csv(output_csv_path, sep=' ', index=False, header=False)

print(f"CSV file saved to: {output_csv_path}")