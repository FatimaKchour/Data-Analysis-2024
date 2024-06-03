import pandas as pd

def create_glance_database(input_file_path, output_file_path):
    # Load the data from the Excel file
    data = pd.read_excel(input_file_path)

    # Extract the relevant columns
    df = data[['TIMESTAMP_INITIAL', 'TIMESTAMP_FINAL', 'GLANCE_DURATION_milliseconds', 'ID_GAZE_CLASS', 'GAZE_QUADRANT']].copy()

    # Remove rows with any missing values in the relevant columns
    df.dropna(subset=['TIMESTAMP_INITIAL', 'TIMESTAMP_FINAL', 'GLANCE_DURATION_milliseconds', 'ID_GAZE_CLASS', 'GAZE_QUADRANT'], inplace=True)

    # Save the dataframe to a new Excel file
    df.to_excel(output_file_path, index=False)

    print(f"Filtered database has been created and saved to {output_file_path}")

# Example usage:
input_file_path = 'path/to/your/input_excel_file.xlsx'  # Replace with your input file path
output_file_path = 'path/to/your/output_excel_file.xlsx'  # Replace with your desired output file path

create_glance_database(input_file_path, output_file_path)
