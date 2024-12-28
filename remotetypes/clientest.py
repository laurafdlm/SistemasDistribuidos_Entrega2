"""Authentication service application."""

import logging
import sys
import time
import os
from remotetypes.json_server import JsonProducer
from remotetypes.json_client import JsonConsumer
from datetime import datetime

def Clientest():
    g=open("./datos/resultado.txt","w+")
    datlist=list()
    producir=JsonProducer()
    consumir=JsonConsumer()
    with open("./datos/source.txt","r") as f:
        while line :=f.readline():
            dato=line.split(" ")
            print (dato[0])
            try:
                datmp=dato[2].replace('\n', '')
            except:
                if dato[0]=='00000000\n':
                    g.write('00000000')
                    print("Final")
                    return(0)
                else:
                    print("Dato erroneo")
                    return(1) 
            if dato[1] =="Set":
                valor=set(datmp.split(','))
                print (valor)
                print(type(valor))
                valor=""
                for i in datmp.split(','):
                    ident=datetime.today().strftime('%y%m%d%H%M%S%f')
                     valores=dict(ident=ident,
                        object_identifier=dato[0],
                        object_type=dato[1],
                        operation=valor,datos=i)
                    producir.putoperation("mi_pruebas10",valores)
                    time.sleep(2)
                    resultados=consumir.getval(ident)
                ident=datetime.today().strftime('%y%m%d%H%M%S%f')
                valores=dict(ident=ident,
                    object_identifier=dato[0],
                    object_type=dato[1]
                    operation="savetofile",datos="")
                producir.putoperation("mi_pruebas10",valores)
                time.sleep(2)
                resultados=consumir.getval(ident)
                salva=dato[0]+' '+dato[1]+' '+resultados["idvalor"]
                g.write( salva + "\n")
            if dato[1] =="List":
                valor=list(datmp.split(','))
                print (valor)
                print(type(valor))
                for i in datmp.split(','):
                    ident=datetime.today().strftime('%y%m%d%H%M%S%f')
                    valores=dict(ident=ident,
                        object_identifier=dato[0],
                        object_type=dato[1],
                        operation=valor,datos=i)
                    producir.putoperation("mi_pruebas10",valores)
                    time.sleep(2)
                    resultados=consumir.getval(ident)
                ident=datetime.today().strftime('%y%m%d%H%M%S%f')
                valores=dict(ident=ident,
                    object_identifier=dato[0],
                    object_type=dato[1]
                    operation="savetofile",datos="")
                producir.putoperation("mi_pruebas10",valores)
                time.sleep(2)
                resultados=consumir.getval(ident)
                salva=dato[0]+' '+dato[1]+' '+resultados["idvalor"]
                g.write( salva + "\n")
            if dato[1] =="Dict":
                valor=dict(item.split(':')
                for item in datmp.split(','))
                print (valor)
                print(type(valor))
                for i in datmp.split(','):
                    j=i.split(':')
                    valtmp=dict{j[0]=j[1])
                    ident=datetime.today().strftime('%y%m%d%H%M%S%f')
                     valores=dict(ident=ident,
                        object_identifier=dato[0],
                        object_type=dato[1],
                        operation=valor,datos=i)
                    producir.putoperation("mi_pruebas10",valtmp)
                    time.sleep(2)
                    resultados=consumir.getval(ident)
                ident=datetime.today().strftime('%y%m%d%H%M%S%f')
                valores=dict(ident=ident,
                    object_identifier=dato[0],
                    object_type=dato[1]
                    operation="savetofile",datos="")
                producir.putoperation("mi_pruebas10",valores)
                time.sleep(2)
                resultados=consumir.getval(ident)
                salva=dato[0]+' '+dato[1]+' '+resultados["idvalor"]
                g.write( salva + "\n")
    f.close()
    g.close()

