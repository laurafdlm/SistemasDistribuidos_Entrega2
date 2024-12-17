import logging
import sys
import Ice
import time
from typing import List
import RemoteTypes as rt 

from remotetypes.clientest import Clientest
from remotetypes.clientverify import Clientverify
class ClientApp(Ice.Application):
    def run(self, args: List[str]) -> int:
        with Ice.initialize("./config/client.config") as communicator:
            while True:
                valor=Clientest(communicator)
                print(valor)
                if valor==0:
                    valor=Clientverify(communicator)
                break
def main():
    appclient = ClientApp()
    return appclient.main(sys.argv)
