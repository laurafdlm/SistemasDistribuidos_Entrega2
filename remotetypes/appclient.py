import logging
import sys
import time
from typing import List

from remotetypes.clientrt import Clientrt

class ClientApp():
    def main(self, args: List[str]) -> int:
        if len(args) != 3:
            print("remotetypes-client topic_name server_kafka")
            return 1
        topic_name=args[1]
        server_kafka=args[2]
        while True:
            valor=Clientrt(topic_name,server_kafka)
            if valor==0:
                break
def main():
    appclient = ClientApp()
    return appclient.main(sys.argv)
