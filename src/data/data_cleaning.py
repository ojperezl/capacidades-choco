import pandas as pd
import pickle

# Cargar el diccionario desde el archivo
with open('data/interim/dataframes.pkl', 'rb') as file:
    dict_dataframes = pickle.load(file)

# Mostrar los nombres de los DataFrames
print(dict_dataframes.keys())

for key, df in dict_dataframes.items():
    # Eliminar la primera fila
    df = df.iloc[1:]

    # Convertir número a texto las columnas "Código Departamento" y "Código Entidad"
    df['Código Departamento'] = df['Código Departamento'].astype(int)
    df['Código Entidad'] = df['Código Entidad'].astype(int)

    # Convertir las columnas "Año" y "Mes" a texto antes de limpiar
    df['Año'] = df['Año'].astype(int)
    df['Mes'] = df['Mes'].astype(int)

    # Asegurarse de que la columna "Dato Numérico" sea de tipo numérico
    #df['Dato Numérico'] = pd.to_numeric(df['Dato Numérico'], errors='coerce')
    #df['Dato Numérico'] = df['Dato Numérico'].str.replace(',', '.').astype(float)

    # Guardar el DataFrame modificado de nuevo en el diccionario
    dict_dataframes[key] = df


# Guardar el diccionario depurado en un archivo
with open('data/processed/dict_dataframes.pkl', 'wb') as file:
    pickle.dump(dict_dataframes, file)


# End.