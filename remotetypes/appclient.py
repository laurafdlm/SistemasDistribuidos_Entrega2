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
                Clientrt(communicator)

def main():
    appclient = ClientApp()
    return appclient.main(sys.argv)
