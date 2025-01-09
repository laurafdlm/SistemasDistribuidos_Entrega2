from confluent_kafka.admin import AdminClient, NewTopic

class TopicManager:
    def __init__(self, bootstrap_servers):
        self.admin_client = AdminClient({'bootstrap.servers': bootstrap_servers})

    def create_topic(self, topic_name, num_partitions=1, replication_factor=1, retention_ms=0):
        config = {}
        if retention_ms is not None:
            config['retention.ms'] = str(retention_ms)
        
        new_topic = NewTopic(
            topic_name,
            num_partitions=num_partitions,
            replication_factor=replication_factor,
            config=config
        )

        # Crear el tópico
        fs = self.admin_client.create_topics([new_topic])

        # Verificar resultados
        for topic, f in fs.items():
            try:
                f.result()  # Llamar para esperar la operación
                print(f"Tópico '{topic}' creado exitosamente.")
            except Exception as e:
                print(f"Error al crear el tópico '{topic}': {e}")

    def delete_topic(self, topic_name):
        # Solicitar la eliminación del tópico
        fs = self.admin_client.delete_topics([topic_name], operation_timeout=30)

        # Verificar resultados
        for topic, f in fs.items():
            try:
                f.result()  # Llamar para esperar la operación
                print(f"Tópico '{topic}' eliminado exitosamente.")
            except Exception as e:
                print(f"Error al eliminar el tópico '{topic}': {e}")
# Ejemplo de uso
if __name__ == "__main__":
   # Configurar el gestor de tópicos
    bootstrap_servers = bootstrap_servers
    topic_manager = TopicManager(bootstrap_servers)

    # Crear un tópico con retención de 1 segundo
    topic_name = 'prueba5_topic'
    topic_manager.create_topic(topic_name, num_partitions=1, replication_factor=1, retention_ms=None)

    # Eliminar el tópico
    topic_manager.delete_topic(topic_name)


