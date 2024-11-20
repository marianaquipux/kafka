import pandas as pd
from sqlalchemy import create_engine
import json

# Configuración de conexión a PostgreSQL
host = 'localhost'  # Cambia si tu PostgreSQL está en otro host
port = '5432'  # Puerto por defecto de PostgreSQL
dbname = 'salazarPostgres'  # Nombre de la base de datos
user = 'admin'  # Tu usuario de PostgreSQL
password = 'root'  # Tu contraseña de PostgreSQL

# Ruta del archivo CSV
csv_file_path = 'medicamentos.csv'

# Crear conexión a PostgreSQL usando SQLAlchemy
engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{dbname}')

# Leer el archivo CSV con pandas
df = pd.read_csv(csv_file_path)
print(df)

# Subir el DataFrame a PostgreSQL (se crea la tabla automáticamente)
df.to_sql('medicamentos', engine, if_exists='replace', index=False)

print(f"Datos cargados exitosamente en la tabla 'medicamentos'.")
