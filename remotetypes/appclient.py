import logging
import sys
import time
from typing import List

from remotetypes.clientrt import Clientrt

class ClientApp():
    def run(self, args: List[str]) -> int:
        while True:
            valor=Clientrt()
            if valor==0:
                break
def main():
    appclient = ClientApp()
    return appclient.main(sys.argv)
