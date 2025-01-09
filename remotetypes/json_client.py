#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# A simple example demonstrating use of JSONDeserializer.

import argparse
import json

from confluent_kafka import Consumer
class JsonConsumer():

    def __init__(self) -> None:
        self.ldata=[]

    def getval(self,topic,server,idgrupo):

        consumer_conf = {'bootstrap.servers': server,
                     'group.id': idgrupo,
                     'auto.offset.reset': "earliest",
                     'enable.auto.commit': True,}

        consumer = Consumer(consumer_conf)
        consumer.subscribe([topic])

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
                self.ldata.append(dict(data))
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
            self.ldata.clear()
            while True:
                # Realizar el polling (espera máximo 1 segundo)
                msg = consumer.poll(1.0)

                if msg is None:
                    # No hay mensajes disponibles, continuar
                    break
                if msg.error():
                    print("All brokers are down! Retrying...")
                    break
                # Si no hay errores, manejar el mensaje
                handle_message(msg)
        except KeyboardInterrupt:
            print("Consumer stopped by user.")

        # Asegurarse de cerrar el consumidor
        print("Closing consumer...")
        consumer.close()
        return(self.ldata)
