"""Authentication service application."""

import logging
import sys
import time
import os
from remotetypes.json_server import JsonProducer
from remotetypes.json_client import JsonConsumer
from datetime import datetime

def Clientverify():
    global datos
    global shaold
    producir=JsonProducer()
    consumir=JsonConsumer()
    g=open("./datos/comprobado.txt","w+")
    with open("./datos/resultado.txt","r") as f:
        while line :=f.readline():
            dato=line.split(" ")
            print (dato[0])
            try:
                datmp=dato[2].replace('\n', '')
            except:
                print("Final o dato erroneo")
                return(0)
            if dato[1] =="Set":
                valor=""
                ident=datetime.today().strftime('%y%m%d%H%M%S%f')
                valores=dict(ident=ident,
                    object_identifier=dato[0],
                    object_type=dato[1]
                    operation="pop",datos="88888888")
                producir.putoperation("mi_pruebas10",valores)
                time.sleep(2)
                resultados=consumir.getval(ident)
                salva=dato[0]+' '+dato[1]+' '+resultados['result']
                g.write( salva + "\n")
            if dato[1] =="List":
                valor=""
                ident=datetime.today().strftime('%y%m%d%H%M%S%f')
                valores=dict(ident=ident,
                    object_identifier=dato[0],
                    object_type=dato[1]
                    operation="pop",datos=88888888)
                producir.putoperation("mi_pruebas10",valores)
                time.sleep(2)
                resultados=consumir.getval(ident)
                salva=dato[0]+' '+dato[1]+' '+resultados['result']
                g.write( salva + "\n")
            if dato[1] =="Dict":
                valor=""
                ident=datetime.today().strftime('%y%m%d%H%M%S%f')
                valores=dict(ident=ident,
                    object_identifier=dato[0],
                    object_type=dato[1]
                    operation="pop",datos="88888888")
                producir.putoperation("mi_pruebas10",valores)
                time.sleep(2)
                resultados=consumir.getval(ident)
                salva=dato[0]+' '+dato[1]+' '+resultados['result']
                g.write( salva + "\n")
    f.close()
    g.close()
