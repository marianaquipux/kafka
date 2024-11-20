from kafka import KafkaAdminClient
from kafka.admin import NewTopic

# Configura el cliente administrador de Kafka
client = KafkaAdminClient(
    bootstrap_servers= ["localhost:9092", "localhost:9094"]
)
# Nombre del tópico que quieres crear
topic_name = "medicamentos"
# Crear un nuevo tópico
new_topic = NewTopic(
    name=topic_name,  # Nombre del tópico
    num_partitions=2,  # Número de particiones
    replication_factor=2,  # Factor de replicación
)
# Crear el tópico en Kafka
client.create_topics([new_topic])
print(f"Tópico '{topic_name}' creado exitosamente.")
# Cerrar la conexión del cliente
client.close()
