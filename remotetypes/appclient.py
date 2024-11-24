import logging
import sys
import Ice
import time
from typing import List
import RemoteTypes as rt 

from remotetypes.clientrt import Clientrt

class ClientApp(Ice.Application):
    def run(self, args: List[str]) -> int:
        with Ice.initialize("./config/client.config") as communicator:
            while True:
                valor=Clientrt(communicator)
                if valor==0:
                    break
def main():
    appclient = ClientApp()
    return appclient.main(sys.argv)
