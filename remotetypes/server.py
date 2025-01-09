"""remotetypes server application."""

import logging

from remotetypes.factory import Factory
from remotetypes.iterable import Iterable
from remotetypes.json_client import JsonConsumer
from remotetypes.json_crear import TopicManager
import time
import os.path
import os, sys
import json

class Server():
    def __init__(self) -> None:
        self.olddatos={'0':'0'}
        self._iteratio = Iterable()
        super().__init__()
        self.logger = logging.getLogger(__file__)
        """Initialise the Server objects."""
        super().__init__()
        self.logger = logging.getLogger(__file__)
    def run(self, args: list[str]) -> int:
        if len(args) != 3:
            print("remotetypes topic_name server_kafka")
            return 1
        factory=Factory()
        consumir=JsonConsumer()
        topic_name=args[1]
        server_kafka=args[2]
        newtopic=TopicManager(server_kafka)
        newtopic.create_topic(topic_name)
        print("Server_Kafka={},Topic_name={}".format(server_kafka,topic_name))
        while True:
            resultados=consumir.getval(topic_name,server_kafka,topic_name)
            if resultados != []:
                for i in resultados:
                    idobject=i["object_identifier"]
                    path='./datos/'+idobject
                    if os.path.isfile(path):
                        iteratio=idobject
                    else:
                        if idobject in self.olddatos:
                            iteratio=self.olddatos[idobject]
                            i["object_identifier"]=iteratio
                        else:
                            iteratio=self._iteratio.next()
                            if iteratio == '00000000':
                                print ('Error valor iteration > 200000')
                                return False
                            self.olddatos[idobject]=iteratio
                            i["object_identifier"]=iteratio
                    print(iteratio)
                    estado=factory.get(i,server_kafka)
            try:
                time.sleep(2)
            except KeyboardInterrupt:
                print ("Crtl+C Pressed. Shutting down.")
                newtopic.delete_topic(topic_name)
                return 0
            # your code here
        return 0
