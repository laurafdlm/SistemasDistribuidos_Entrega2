"""Needed classes to implement the Factory interface."""
#import pickle
#from fs.osfs import OSFS
from remotetypes.remotelist import RemoteList
from remotetypes.remoteset import RemoteSet
from remotetypes.remotedict import RemoteDict
from remotetypes.iterable import Iterable
from remotetypes.json_server import JsonProducer
from remotetypes.json_client import JsonConsumer
import time
import os.path
import os, sys

class Factory():

    def __init__(self) -> None:
        """Initialise the Server objects."""
        super().__init__()
        self.logger = logging.getLogger(__file__)
    def run(self, args: list[str]) -> int:
        producir=JsonProducer()
        consumir=JsonConsumer()
        factory=Factory()
        while True:
            resultados=consumir.getval('mi_pruebas10')
            if resultados != "":
                for i in resultados:
                    estado=factory.get(i)
            time.sleep(1)
            # your code here

    """Skeleton for the Factory implementation."""
    def get(self,datos):
        ident=datos["ident"]
        typename=datos["object_type"]
        opt1=datos["object_identifier"]
        operador=datos["operation"]
        if typename == "RSet":
            msg=datos["datos"]
            if len(opt1) != 0 :
                path='./datos/'+opt1
                if not os.path.isfile(path):
                     iteratio='00000000'
                else:
                    iteratio=opt1
            else:
                iteratio=self._iteratio.next()
            if iteratio == '00000000':
                print ('Error valor no existe o iteration > 200000')
                return False
            print(iteratio)
            newiter=int(iteratio)
            rdato=RemoteSet(newiter)
            if operador == "remove":
                rtdato.remove(msg)
            if operador == "length":
                valor=rtdato.length()
            if operador == "contains":
                valor=rtdato.contains(msg)
            if operador == "hash":
                valor=rtdato.hash()
            if operador == "add":
                rtdato.add(msg)
            if operador == "pop":
                valor=rtdato.pop()
            if operador =="savetofile":
                rtdato.savetofile()
            dvalores=dict(ident=ident,status="ok",result=valor,idvalor=iteratio,error="")
            producir.putresultado(ident,dvalores)            
            return True

        if typename == "RList":
            msg=datos["datos"]
            if len(opt1) != 0 :
                path='./datos/'+opt1
                if not os.path.isfile(path):
                     iteratio='00000000'
                else:
                    iteratio=opt1
            else:
                iteratio=self._iteratio.next()
            if iteratio == '00000000':
                print ('Error valor no existe o iteration > 200000')
                return False
            newiter=int(iteratio)
            rdato=RemoteList(newiter)
            if operador == "remove":
                rtdato.remove(msg)
            if operador == "length":
                valor=rtdato.length()
            if operador == "contains":
                valor=rtdato.contains(msg)
            if operador == "hash":
                valor=rtdato.hash()
            if operador == "append":
                rtdato.append(msg)
            if operador == "pop":
                valor=rtdato.pop(msg)
            if operador =="savetofile":
                rtdato.savetofile()
            dvalores=dict(ident=ident,status="ok",result=valor,idvalor=iteratio,error="")
            producir.putresultado(ident,dvalores)            
            return True

        if typename == "RDict":
            msg=datos["datos"]
            for i,j in msg.items():
                msg1=i
                msg2=j
            if len(opt1) != 0 :
                path='./datos/'+opt1
                if not os.path.isfile(path):
                     iteratio='00000000'
                else:
                    iteratio=opt1
            else:
                iteratio=self._iteratio.next()
            if iteratio == '00000000':
                print ('Error valor no existe o iteration > 200000')
                return False
            newiter=int(iteratio)
            rdato=RemoteDict(newiter)
            if operador == "remove":
                rtdato.remove(msg1)
            if operador == "length":
                valor=rtdato.length()
            if operador == "contains":
                valor=rtdato.contains(msg1)
            if operador == "hash":
                valor=rtdato.hash()
            if operador == "setItem":
                valor=rtdato.setItem(msg1,msg2)
            if operador == "getItem":
                valor=rtdato.getItem(msg1)
            if operador == "pop":
                valor=rtdato.pop(msg1)
            if operador =="savetofile":
                rtdato.savetofile()
            dvalores=dict(ident=ident,status="ok",result=valor,idvalor=iteratio,error="")
            producir.putresultado(ident,dvalores)
            return True

    def __init__(self):
        self._nextId = 0
        self._iteratio = Iterable()
