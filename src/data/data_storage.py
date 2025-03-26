import os
import pandas as pd
import pickle

# Cargar el diccionario de DataFrames
with open('data/processed/dict_dataframes.pkl', 'rb') as file:
    dict_dataframes = pickle.load(file)

# Importar dimensiones capacidades
nombre_archivos = pd.read_csv('data/manual/nombre-archivos.csv', sep=';')

# Crear un diccionario para mapear "Nombre original" a "Nombre archivo"
name_mapping = dict(zip(nombre_archivos['Nombre original'], nombre_archivos['Nombre archivo']))

# Crear un diccionario para mapear "Nombre original" a "Dimensión capacidades"
dimension_mapping = dict(zip(nombre_archivos['Nombre original'], nombre_archivos['Dimensión capacidades']))

# Renombrar y guardar los DataFrames
for name, df in dict_dataframes.items():
    # Reemplazar el nombre del DataFrame usando el mapeo
    new_name = name_mapping.get(name, name)  # Si no encuentra el nombre, usa el original
    dimension_folder = dimension_mapping.get(name, "default")  # Carpeta por defecto si no encuentra la dimensión

    # Crear la carpeta si no existe
    folder_path = os.path.join('data/processed', dimension_folder)
    os.makedirs(folder_path, exist_ok=True)

    # Guardar el DataFrame en la carpeta correspondiente
    file_path = os.path.join(folder_path, f"{new_name}.csv")
    df.to_csv(file_path, index=False, decimal=',')


# End.
