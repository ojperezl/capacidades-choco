import os
import pandas as pd
import pickle

# Define the __file__ variable if it is not already defined
if '__file__' not in globals():
    __file__ = os.path.abspath('make_dataset.py')

# Define the path to the raw data folder
raw_data_path = os.path.join(os.path.dirname(__file__), 'data/raw')
processed_data_path = os.path.join(os.path.dirname(__file__), 'data/interim')

# List all .xlsx files in the raw data folder
xlsx_files = [f for f in os.listdir(raw_data_path) if f.endswith('.xlsx')]

# Create a dictionary to store DataFrames
dataframes = {}

# Loop through each file, convert it to CSV, and read it into a DataFrame
for file in xlsx_files:
    # Remove the "TerriData_" prefix and the file extension to get the DataFrame name
    df_name = file.replace('TerriData_', '').replace('.xlsx', '')
    # Read the Excel file into a DataFrame
    df = pd.read_excel(os.path.join(raw_data_path, file), decimal=',')
    # Convert the DataFrame to a CSV file
    csv_file_path = os.path.join(processed_data_path, f"{df_name}.csv")
    df.to_csv(csv_file_path, index=False)
    # Read the CSV file into a DataFrame with specified dtype
    df = pd.read_csv(csv_file_path, dtype={8: str}, low_memory=False)
    # Store the DataFrame in the dictionary
    dataframes[df_name] = df

# Now you can access each DataFrame by its name in the `dataframes` dictionary
# For example, to access the DataFrame for a file named "TerriData_example.xlsx", use `dataframes['example']`

# Guardar el diccionario en un archivo
with open('data/interim/dataframes.pkl', 'wb') as file:
    pickle.dump(dataframes, file)


# End.