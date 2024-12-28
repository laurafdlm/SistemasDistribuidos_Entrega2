# A simple example demonstrating use of JSONSerializer.

from uuid import uuid4

from six.moves import input

from confluent_kafka import Producer
from confluent_kafka.serialization import StringSerializer, SerializationContext, MessageField
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.json_schema import JSONSerializer
import json
class JsonProducer():
    class User(object):
        """
        User record

        Args:
            ident (int): Identificador unico de la operacion

            object_identifier (str): Identificador del Objeto

            object_type (str): Tipo de Objeto

            operation (str): Nombre del metodo que se ejcuta

            args (object): Valores o Datos

            """
        def __init__(self, ident, object_identifier, object_type, operation, datos):
            self.ident = ident
            self.object_identifier = object_identifier
            self.object_type=object_type
            self.operation=operation
            self.datos=datos

    def user_to_dict(user, ctx):
        """
        Returns a dict representation of a User instance for serialization.

        Args:
            user (User): User instance.

            ctx (SerializationContext): Metadata pertaining to the serialization
                operation.

        Returns:
            dict: Dict populated with user attributes to be serialized.
        """

        # User._address must not be serialized; omit from dict
        return dict(ident=user.ident,
                    object_identifier=user.object_identifier,
                    object_type=user.object_type,operation=user.operation,datos=user.datos)

    def putoperation(self,topic,valores):
        # topic(str), valores(dict)
        schema_str = """
        {
            "$schema": "http://json-schema.org/draft-07/schema#",
            "type": "object",
            "properties": {
                "ident": {
                    "type": "string",
                    "description": "Identificador único de la operación",
                    "uniqueItems": true
                    },
                "object_identifier": {
                    "type": "string",
                    "description": "Identificador del objeto sobre el que se ejecutará la operación",
                    g"maxLength": 8
                    },
                "object_type": {
                    "type": "string",
                    "enum": ["RSet", "RList", "RDict"],
                    "description": "Tipo de objeto: RSet, RList o RDict."
                    },
                "operation": {
                    "type": "string",
                    "description": "Nombre del método que se ejecutará sobre el objeto.",
                    "oneOf": [
                        {
                            "if": { "properties": { "object_type": { "const": "RSet" } } },
                            "then": { "enum": ["remove", "length", "contains", "hash", "add", "pop", "savetofile"] }
                        },
                        {   
                            "if": { "properties": { "object_type": { "const": "RList" } } },
                            "then": { "enum": ["remove", "length", "contains", "hash", "append", "pop", "getItem", "savetofile"] }
                        },
                        {
                            "if": { "properties": { "object_type": { "const": "RDict" } } },
                            "then": { "enum": ["remove", "length", "contains", "hash", "setItem", "getItem", "pop", "savetofile"] }
                        }
                            ]
                },
                "datos": {
                    "description": "Argumentos necesarios para la operación, definidos como un objeto JSON.",
                    "oneOf":	[
                        {
                            "if": { "properties": { "object_type": { "enum": ["RSet", "RList"] } } },
                            "then": { "type": "array", "items": { "type": "string" }, "description": "Array de strings para RSet y RList" }
                        },
                        {
                            "if": { "properties": { "object_type": { "const": "RDict" } } },
                            "then": { "type": "object", "additionalProperties": true, "description": "Objeto key-value para RDict." }
                        }
                                ]
                    }
            },
            "required": ["ident", "object_identifier", "object_type", "operation"],
            "additionalProperties": false
        }

        """
        schema_registry_conf = {'url': "http://kafka:8085"}
        schema_registry_client = SchemaRegistryClient(schema_registry_conf)

        string_serializer = StringSerializer('utf_8')
        json_serializer = JSONSerializer(schema_str, schema_registry_client, user_to_dict)

        producer = Producer({'bootstrap.servers': "kafka"})

        print("Producing user records to topic {}. ^C to exit.".format(topic))
        while True:
            # Serve on_delivery callbacks from previous calls to produce()
            producer.poll(0.0)
            try:
                user = User(ident=valores["ident"],
                            object_identifier=valores["object_identifier"],
                            object_type=valores["object_type"],
                            operation=valores["operation"],datos=valores["datos"])
                dictuser=json.dumps(valores).encode("utf-8")
                value=json_serializer(user, SerializationContext(topic, MessageField.VALUE))
                producer.produce(topic=topic, key=string_serializer(str(uuid4())), value=dictuser, partition=0)
            except KeyboardInterrupt:
                break
            except:
                print("Invalid input, discarding record...")
                continue

        print("\nFlushing records...")
        producer.flush()

    def putresultado(self,topic,valores):
        # topic(str), valores(dict)
        schema2_str = """
        {
            "$schema": "http://json-schema.org/draft-07/schema#",
            "type": "object",
            "properties": {
                    "ident": {
                        "type": "string",
                        "description": "Identificador único de la operación",
                        "uniqueItems": true
                    },
                    "status": {
                        "type": "string",
                        "enum": ["ok", "error"],
                        "description": "Estado de la operación: 'ok' si fue exitosa"
                    },
                    "result": {
                        "type": "string",
                        "description": "Resultado devuelto por la operación"
                    },
                    "idvalor": {
                        "type": "string",
                        "description": "ID de la variable"
                    },
                    "error": {
                        "type": "string",
                        "description": "Clase de la excepción en caso de error"
                    }
            },
            "required": ["ident", "status"],
            "additionalProperties": false
        }
        """
        schema_registry_conf = {'url': "http://kafka:8085"}
        schema_registry_client = SchemaRegistryClient(schema_registry_conf)

        string_serializer = StringSerializer('utf_8')
        json_serializer = JSONSerializer(schema_str, schema_registry_client, user_to_dict)

        producer = Producer({'bootstrap.servers': "kafka"})

        print("Producing user records to topic {}. ^C to exit.".format(topic))
        while True:
            # Serve on_delivery callbacks from previous calls to produce()
            producer.poll(0.0)
            try:
                dictresul = dict(ident=user_ident,status="ok",result=valores["object_type"],idvalor=valores["datos"])
                dictresul=json.dumps(dictresul).encode("utf-8")
                producer.produce(topic="resul-" + valores["ident"], key=string_serializer(str(uuid4())), value=dictresul, partition=0)
            except KeyboardInterrupt:
                break
            except:
                print("Invalid input, discarding record...")
                continue

        print("\nFlushing records...")
        producer.flush()

