import pandas as pd
import pickle
import json
import time
import os
from tqdm import tqdm  # Para mostrar barra de progreso

# Crear directorio para resultados parciales si no existe
os.makedirs('reports/partial', exist_ok=True)

# Cargar el diccionario de DataFrames
print("Cargando diccionario de DataFrames...")
with open('data/processed/dict_dataframes.pkl', 'rb') as file:
    dict_dataframes = pickle.load(file)

# Crear un diccionario para almacenar la caracterización
characterization = {}

# Iterar sobre cada DataFrame en el diccionario con barra de progreso
for name in tqdm(dict_dataframes.keys(), desc="Procesando DataFrames"):
    start_time = time.time()
    df = dict_dataframes[name]
    
    # Extraer la información requerida de manera optimizada
    dim_values = df["Dimensión"].unique().tolist() if "Dimensión" in df.columns else []
    sub_values = df["Subcategoría"].unique().tolist() if "Subcategoría" in df.columns else []
    ind_values = df["Indicador"].unique().tolist() if "Indicador" in df.columns else []
    
    # Calcular años mínimo y máximo solo si la columna existe
    year_min = None
    year_max = None
    if "Año" in df.columns:
        if not df["Año"].empty:
            try:
                year_min = df["Año"].min()
                year_max = df["Año"].max()
            except:
                pass
    
    # Extraer fuentes y unidad de medida
    fuentes_values = df["Fuentes"].unique().tolist() if "Fuentes" in df.columns else []
    umedida_values = df["Unidad de Medida"].unique().tolist() if "Unidad de Medida" in df.columns else []
    
    # Guardar resultados en el diccionario
    characterization[name] = {
        "Dimensión": dim_values,
        "Subcategoría": sub_values,
        "Indicador": ind_values,
        "Año (min)": year_min,
        "Año (max)": year_max,
        "Fuentes": fuentes_values,
        "Unidad de Medida": umedida_values
    }
    
    # Guardar resultados parciales
    partial_filename = f'reports/partial/characterization_{name}.json'
    with open(partial_filename, 'w') as json_file:
        json.dump({name: characterization[name]}, json_file, indent=4, ensure_ascii=False)
    
    end_time = time.time()
    print(f"Procesado {name} en {end_time - start_time:.2f} segundos")


# Actualizar nombres de archivos en el archivo JSON de caracterización
#---------------------------------------------------------------------

# Cargar el dataframe con los nombres de archivos
nombre_archivos = pd.read_csv('data/manual/nombre-archivos.csv', sep=';')

# Crear un diccionario de mapeo: nombre original -> nuevo nombre
name_mapping = dict(zip(
    nombre_archivos['Nombre original'], 
    nombre_archivos['characterization']
))

# Crear un nuevo diccionario con los nombres actualizados
updated_characterization = {}

# Reemplazar los nombres 
for old_name, data in characterization.items():
    # Si el nombre original está en el mapeo, usar el nuevo nombre, sino mantener el original
    new_name = name_mapping.get(old_name, old_name)
    updated_characterization[new_name] = data

# Guardar el JSON actualizado
with open('reports/characterization/characterization.json', 'w') as file:
    json.dump(updated_characterization, file, indent=4, ensure_ascii=False)


# End.