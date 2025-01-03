# A simple example demonstrating use of JSONSerializer.

from uuid import uuid4

from six.moves import input

from confluent_kafka import Producer
from confluent_kafka.serialization import StringSerializer, SerializationContext, MessageField
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.json_schema import JSONSerializer
import json

class JsonProducer():
    def putval(self,topic,server_kafka,valores):
        # topic(str), valores(dict)

        string_serializer = StringSerializer('utf_8')

        producer = Producer({'bootstrap.servers': server_kafka})

        print("Producing user records to topic {}. ^C to exit.".format(topic))
        # Serve on_delivery callbacks from previous calls to produce()
        producer.poll(0.0)
        try:
            dictuser=json.dumps(valores).encode("utf-8")
            producer.produce(topic=topic, key=string_serializer(str(uuid4())), value=dictuser, partition=0)
        except KeyboardInterrupt:
            return 1 
        except:
            print("Invalid input, discarding record...")
            return 1
        print("\nFlushing records...")
        producer.flush()
        return 0
