# Análisis cuantitativo para la caracterización sociodemográfica y económica de la población femenina en el departamento del Chocó a partir del enfoque de capacidades

El presente repositorio documenta el desarrollo del análisis cuantitativo para la caracterización sociodemográfica de las mujeres en el Chocó, con especial atención en Quibdó e Itsmina. El marco teórico define conceptos clave como capacidades, funcionamientos y libertades como guías para la caracterización sociodemográfica y económica. 

En este repositorio se encuentra el desarrollo de la caracterización, incluyendo bases, scripts y la categorización de la información disponible en Colombia para alinearse con el enfoque de las capacidades. El objetivo consiste en documentar el proceso cuantitativo, así como permitir tanto la auditoría de los resultados como de su reproductibilidad.

## Etapas del análisis

Se definieron cinco etapas para el desarrollo de la caracterización sociodemográfica, y que se especifican a continuación. 

### 1. Identificar principales fuentes de información e indicadores

Sobre los criterios definidos en el proyecto se realizó la búsqueda de información que cumpliera con los criterios de calidad, espacio temporal, representatividad y disponibilidad. La principal referencia en ese sentido ha sido la plataforma Terridata del Departamento Nacional de Planeación (DNP) para extraer datos cuantitativos relevantes y representativos.

Terridata es una herramienta desarrollada para facilitar la visualización, consulta y análisis de datos estadísticos a nivel municipal, departamental y regional. Su principal objetivo es proporcionar indicadores estandarizados y comparables que reflejen los resultados en diversas dimensiones socioeconómicas de las entidades territoriales del país. La plataforma cuenta con más de 800 indicadores organizados en 16 dimensiones.

- Se exploraron las diferentes dimensiones y subcategorías ofrecidas en Terridata, evaluando cada indicador en función de su pertinencia para analizar la participación política y la movilización social estudiadas.
- Se seleccionaron aquellos indicadores que cumplían con los criterios establecidos, asegurando la coherencia y relevancia de la información para el estudio.
- Se documentó el proceso de selección, permitiendo la trazabilidad y verificación de las fuentes de información utilizadas.

### 2. Tratamiento de las Bases de Datos (BBDD)

En esta etapa se procesó la información descargada para garantizar que los datos fueran confiables y adecuados para el análisis. Se realizaron las siguientes acciones:
- Carga de Información: Se importaron los datos obtenidos de Terridata, asegurando la correcta lectura y formato de la información.
- Revisión y Limpieza: Se revisaron los registros para identificar y corregir errores, eliminar duplicados y normalizar las variables, asegurando la consistencia de los indicadores socioeconómicos y demográficos.
- Caracterización: Se aplicaron criterios de categorización y se evaluó la calidad de los datos, facilitando su posterior análisis y generación de resultados precisos.
- Almacenamiento: La base de datos final se estructuró y almacenó en formatos estandarizados, permitiendo su consulta y manipulación en etapas posteriores del estudio.

Los scripts con estas tareas se encuentra en la carpeta src/data/ del repositorio. De igual manera, en la carpeta reports/characterization/ se encuentra la caracterización de cada una de las bases de datos con los indicadores por las dimensiones definidas por el sistema Terridata.

### 3. Categorización de la información por dimensiones

Los indicadores seleccionados, se organizaron por dimensiones, siguiendo los criterios del enfoque de capacidades. Se priorizaron aquellos con mayor relevancia para caracterizar las capacidades fundamentales de Nussbaum: vida, salud corporal, afiliación, razón práctica, control sobre el entorno propio, entre otras.

#### Clasificación por Dimensiones:
Los indicadores se agruparon según su alineación con las capacidades centrales propuestas en el enfoque teórico.
- Bienestar material y sustento
- Capacidades básicas de vida y salud
- Contexto social y demográfico
- Desarrollo cognitivo y libertad de pensamiento
- obernanza y participación civil
- Integridad y seguridad personal

El documento *Análisis de la información cuantitativa disponible* presenta la discusión respecto a estas dimensiones y su pertinencia para la caracterización sociodemográfica. El documento se encuentra en el Drive (Caracterización sociodemográfica/1. Fuentes de información/). De igual manera, en la carpeta /data/manual/ del presente directorio se encuentran las tablas que sirvieron de soporte para realizar la clasificación de los indicadores en estas nuevas dimensiones.

#### Análisis Contextual:
Se evaluó la pertinencia de cada indicador en relación con las realidades sociales y económicas del Chocó. En particular, se consideraron datos desagregados por género cuando estaban disponibles.

#### Limitaciones Identificadas:
- Falta de desagregación por género en varios indicadores clave.
- Insuficiencia de datos cualitativos para evaluar percepciones y experiencias subjetivas.
- Enfoque predominante en aspectos económicos y productivos, dejando fuera dimensiones sociales importantes.

### 4. Análisis indicadores


### 5. Modelos de caracterización 
