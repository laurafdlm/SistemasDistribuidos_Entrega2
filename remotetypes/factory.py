"""Needed classes to implement the Factory interface."""
#import pickle
#from fs.osfs import OSFS
from remotetypes.remotelist import RemoteList
from remotetypes.remoteset import RemoteSet
from remotetypes.remotedict import RemoteDict
from remotetypes.iterable import Iterable
from remotetypes.json_server import JsonProducer
import time
import os.path
import os, sys
import json

class Factory():

    def __init__(self) -> None:
        self.olddata=[]
        """Initialise the Server objects."""
    def get(self,datos,server_kafka):
        producir=JsonProducer()
        ident=datos["ident"]
        typename=datos["object_type"]
        iteratio=datos["object_identifier"]
        operador=datos["operation"]
        path='./datos/'+iteratio
        if typename == "Set":
            msg=datos["datos"]
            newiter=int(iteratio)
            rtdato=RemoteSet(newiter)
            path='./datos/'+iteratio
            if os.path.isfile(path):
                with open(path,'r') as f:
                    loaded_set = json.load(f)
                    self.olddata=loaded_set
                    for i in loaded_set:
                        print(i)
                        funcup=i["operation"]
                        valup=i["datos"]
                        if funcup == "remove":
                            rtdato.remove(valup)
                        if funcup == "add":
                            rtdato.add(valup)
                        if funcup == "pop":
                            valor=rtdato.pop()
                valor=rtdato.leervalor()
                print(valor)
            valor=""
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
            if operador =="leervalor":
                valor=rtdato.leervalor()
            dvalores=dict(ident=ident,status="ok",result=valor,idvalor=iteratio,error="")
            producir.putval(ident,server_kafka,dvalores)
            datenv=dict(ident=ident,
                        object_identifier=iteratio,
                        object_type=typename,
                        operation=operador,datos=msg)
            self.olddata.append(datenv)
            with open(path, 'w') as f:
                json.dump(self.olddata, f)

        if typename == "List":
            msg=datos["datos"]
            newiter=int(iteratio)
            rtdato=RemoteList(newiter)
            path='./datos/'+iteratio
            if os.path.isfile(path):
                with open(path,'r') as f:
                    loaded_list = json.load(f)
                    self.olddata=loaded_list
                    for i in loaded_list:
                        print(i)
                        funcup=i["operation"]
                        valup=i["datos"]
                        if funcup == "remove":
                            rtdato.remove(valup)
                        if funcup == "append":
                            rtdato.append(valup)
                        if funcup == "pop":
                            valor=rtdato.pop(valup)
                valor=rtdato.leervalor()
                print(valor)
            valor=""
            if operador == "remove":
                rtdato.remove(msg)
            if operador == "length":
                valor=rtdato.length()
            if operador == "contains":
                valor=rtdato.contains(msg)
            if operador == "hash":
                valor=rtdato.hash()
            if operador == "append":
                print(msg)
                rtdato.append(msg)
            if operador == "pop":
                valor=rtdato.pop(msg)
            if operador == "getItem":
                valor=rtdato.getItem(msg)
            if operador =="leervalor":
                valor=rtdato.leervalor()
            dvalores=dict(ident=ident,status="ok",result=valor,idvalor=iteratio,error="")
            producir.putval(ident,server_kafka,dvalores)
            datenv=dict(ident=ident,
                        object_identifier=iteratio,
                        object_type=typename,
                        operation=operador,datos=msg)
            self.olddata.append(datenv)
            with open(path, 'w') as f:
                json.dump(self.olddata, f)
            return True

        if typename == "Dict":
            msg=datos["datos"]
            newiter=int(iteratio)
            rtdato=RemoteDict(newiter)
            path='./datos/'+iteratio
            if os.path.isfile(path):
                with open(path,'r') as f:
                    loaded_dict = json.load(f)
                    self.olddata=loaded_dict
                    for i in loaded_dict:
                        funcup=i["operation"]
                        valup=i["datos"]
                        if funcup == "remove":
                            rtdato.remove(valup)
                        if funcup == "setItem":
                            try:
                                vartmp=eval(valup)
                            except:
                                vartmp=[None,None]
                            valor=rtdato.setItem(vartmp[0],vartmp[1])
                        if funcup == "pop":
                            valor=rtdato.pop(valup)
                valor=rtdato.leervalor()
                print(valor)
            valor=""
            if operador == "remove":
                rtdato.remove(msg)
            if operador == "length":
                valor=rtdato.length()
            if operador == "contains":
                valor=rtdato.contains(msg)
            if operador == "hash":
                valor=rtdato.hash()
            if operador == "setItem":
                try:
                    vartmp=eval(msg)
                except:
                    vartmp=[None,None]
                rtdato.setItem(vartmp[0],vartmp[1])
            if operador == "getItem":
                valor=rtdato.getItem(msg)
            if operador == "pop":
                valor=rtdato.pop(msg)
            if operador =="leervalor":
                valor=rtdato.leervalor()
            dvalores=dict(ident=ident,status="ok",result=valor,idvalor=iteratio,error="")
            producir.putval(ident,server_kafka,dvalores)
            datenv=dict(ident=ident,
                        object_identifier=iteratio,
                        object_type=typename,
                        operation=operador,datos=msg)
            self.olddata.append(datenv)
            with open(path, 'w') as f:
                json.dump(self.olddata, f)
            return True

