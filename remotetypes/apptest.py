import logging
import sys
import time
from typing import List
import os
import pickle

from remotetypes.clientest import Clientest
#from remotetypes.clientverify import Clientverify
class ClientApp():
    def main(self, args: List[str]) -> int:
        if len(args) != 3:
            print("remotetypes-test topic_name server_kafka")
            return 1
        topic_name=args[1]
        server_kafka=args[2]
        if os.path.isfile("./datos/registro.bin"):
            with open("./datos/registro.bin","rb") as f:
                registro = pickle.load(f)
        else:
            registro=str(random.randint(10000000, 99999999))
        with open("./datos/registro.bin","wb") as f:
            pickle.dump(registro,f)
        with open("./datos/source.txt","r") as f:
            while line :=f.readline():
                dato=line.split(" ")
                iteratio=dato[0]+registro
                print (dato[0])
                try:
                    dato[2]=dato[2].replace('\n', '')
                except:
                    if dato[0]=='00000000\n':
                        g.write('00000000')
                        print("Final")
                        return(0)
                    else:
                        print("Dato erroneo")
                        return(1)
                print(dato[1])
                valor=Clientest(topic_name,server_kafka,iteratio,dato)
                print(valor)
        f.close()
def main():
    appclient = ClientApp()
    return appclient.main(sys.argv)
