import logging
import sys
import time
from typing import List

from remotetypes.clientest import Clientest
from remotetypes.clientverify import Clientverify
class ClientApp():
    def run(self, args: List[str]) -> int:
        while True:
            valor=Clientest()
            print(valor)
            if valor==0:
                valor=Clientverify()
            break
def main():
    appclient = ClientApp()
    return appclient.main(sys.argv)
