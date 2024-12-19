import csv


def dms_to_decimal(deg, min_, sec):
    # Convert to absolute decimal value
    abs_dec = abs(deg) + (min_ / 60.0) + (sec / 3600.0)
    return abs_dec if deg < 0 else abs_dec


def process_txt_to_csv(input_file, output_file):
    """
    Process a text file to extract latitude, longitude, and height,
    convert coordinates to decimal degrees, and save to a CSV file.
    """
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        csv_writer = csv.writer(outfile)
        csv_writer.writerow(["Latitude", "Longitude", "Height"])

        for line in infile:
            parts = line.split()
            if len(parts) < 8:  # Skip lines that don't have enough data
                continue

            try:
                # Extract DMS for latitude and longitude
                lat_d, lat_m, lat_s = map(float, parts[2:5])
                lon_d, lon_m, lon_s = map(float, parts[5:8])

                # Convert to decimal degrees
                lat_decimal = dms_to_decimal(lat_d, lat_m, lat_s)
                lon_decimal = dms_to_decimal(lon_d, lon_m, lon_s)

                # Longitude is negative in the Western Hemisphere
                lon_decimal *= -1

                # Extract height
                height = float(parts[8])

                # Write to CSV
                csv_writer.writerow([lat_decimal, lon_decimal, height])

            except ValueError:
                # Skip any lines with malformed data
                continue


# Input and output file paths
input_file = 'Rover2_PPP_Kinematic.txt'
output_file = 'C:/Users/Nobo/Desktop/UNB/Fourth Year/First Term/GGE5042 Kinematic Positioning/Final Report/Question 2/Data/CSV/Rover2_PPP_Kinematic.csv'

process_txt_to_csv(input_file, output_file)
output_file
