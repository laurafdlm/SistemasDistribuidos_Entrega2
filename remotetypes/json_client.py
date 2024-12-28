#

import argparse
import json

from confluent_kafka import Consumer
class JsonConsumer():
    def getval(self,topic):
        topic=topic
        consumer_conf = {'bootstrap.servers': "kafka",
                     'group.id': 1,
                     'auto.offset.reset': "earliest"}

        consumer = Consumer(consumer_conf)
        consumer.subscribe([topic])
        data=""
        def handle_message(msg):
            """Maneja un mensaje consumido."""
            try:
                # Decodificar el valor del mensaje

                value=msg.value().decode('utf-8')
        
                # Intentar parsear el JSON
                data = json.loads(value)
                print(f"Message processed: {data}")

                # Realizar alguna operación basada en el contenido
                # (Esto dependerá de tus necesidades específicas)
                process_success(data)
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")
                handle_error(f"Invalid JSON format: {e}")

            except Exception as e:
                print(f"Error processing message: {e}")
                handle_error(f"Unexpected error: {e}")

        def handle_error(error_message):
            """Maneja errores encontrados durante el consumo."""
            print('Handling error: ',error_message)
            # Aquí puedes registrar, notificar o realizar alguna acción con los errores

        def process_success(data):
            """Maneja operaciones exitosas."""
            print('Successfully processed data: ',data)

        try:
            print('Starting consumer polling...')
            ldata=list()
            while True:
                # Realizar el polling (espera máximo 1 segundo)
                msg = consumer.poll(1.0)

                if msg is None:
                    # No hay mensajes disponibles, continuar
                    break 

                if msg.error():
                    # Manejar errores de Kafka
                    if msg.error().code() == KafkaError._PARTITION_EOF:
                        # Fin de la partición (no es un error crítico)
                        print("Reached end of partition: ",msg.error())
                    elif msg.error().code() == KafkaError._ALL_BROKERS_DOWN:
                        print("All brokers are down! Retrying...")
                        break
                    else:
                        raise KafkaException(msg.error())

                # Si no hay errores, manejar el mensaje
                ldata.append(msg)
                handle_message(msg)

        except KeyboardInterrupt:
            print("Consumer stopped by user.")

        finally:
            # Asegurarse de cerrar el consumidor
            print("Closing consumer...")
            consumer.close()
            return(ldata)

