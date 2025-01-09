"""Authentication service application."""

import logging
import sys
import time
import os
from remotetypes.json_server import JsonProducer
from remotetypes.json_client import JsonConsumer
from remotetypes.json_crear import TopicManager
from datetime import datetime
import random
import pickle

def Clientest(topic_name,server_kafka,iteratio,dato):
    nuevo=1
    g=open("./datos/resultado.txt","w+")
    datlist=list()
    producir=JsonProducer()
    consumir=JsonConsumer()
    newtopic=TopicManager(server_kafka)
    if dato[1] =="Set":
        resultados=""
        valor="add"
        for i in dato[2].split(','):
            ident='test'+str(random.randint(10000000, 99999999))
            valores=dict(ident=ident,
                object_identifier=iteratio,
                object_type=dato[1],
                operation=valor,datos=str(i))
            producir.putval(topic_name,server_kafka,valores)
            time.sleep(4)
            resultmp=consumir.getval(ident,server_kafka,ident)
            newtopic.delete_topic(ident)
            try:
                resultados=resultmp[0]
            except:
                print("Error Servidor")
                return
            print(resultados)
            if nuevo == 1:
                iteratio=resultados['idvalor']
                nuevo = 0
        resultados=""
        ident='test'+str(random.randint(10000000, 99999999))
        valores=dict(ident=ident,
            object_identifier=iteratio,
            object_type=dato[1],
            operation="leervalor",datos="")
        producir.putval(topic_name,server_kafka,valores)
        time.sleep(4)
        resultmp=consumir.getval(ident,server_kafka,ident)
        newtopic.delete_topic(ident)
        try:
            resultados=resultmp[0]
        except:
            print("Error Servidor")
            return
        print(resultados)
        salva=str(dato[0])+' '+str(dato[1])+' '+str(resultados)
        g.write( salva + "\n")
    if dato[1] =="List":
        resultados=""
        valor='append'
        for i in dato[2].split(','):
            ident='test'+str(random.randint(10000000, 99999999))
            valores=dict(ident=ident,
                object_identifier=iteratio,
                object_type=dato[1],
                operation=valor,datos=str(i))
            producir.putval(topic_name,server_kafka,valores)
            time.sleep(4)
            resultmp=consumir.getval(ident,server_kafka,ident)
            newtopic.delete_topic(ident)
            try:
                resultados=resultmp[0]
            except:
                print("Error Servidor")
                return
            print(resultados)
            if nuevo == 1:
                iteratio=resultados['idvalor']
                nuevo = 0
        resultados=""
        ident='test'+str(random.randint(10000000, 99999999))
        valores=dict(ident=ident,
            object_identifier=iteratio,
            object_type=dato[1],
            operation="leervalor",datos="")
        producir.putval(topic_name,server_kafka,valores)
        time.sleep(4)
        resultmp=consumir.getval(ident,server_kafka,ident)
        newtopic.delete_topic(ident)
        try:
            resultados=resultmp[0]
        except:
            print("Error Servidor")
            return
        print(resultados)
        salva=str(dato[0])+' '+str(dato[1])+' '+str(resultados)
        g.write( salva + "\n")
    if dato[1] =="Dict":
        valor='setItem'
        resultados=""
        for i in dato[2].split(','):
            j=i.split(':')
            valtmp=str([j[0],j[1]])
            ident='test'+str(random.randint(10000000, 99999999))
            valores=dict(ident=ident,
                object_identifier=iteratio,
                object_type=dato[1],
                operation=valor,datos=valtmp)
            producir.putval(topic_name,server_kafka,valores)
            time.sleep(4)
            resultmp=consumir.getval(ident,server_kafka,ident)
            newtopic.delete_topic(ident)
            try:
                resultados=resultmp[0]
            except:
                print("Error Servidor")
                return
            print(resultados)
            if nuevo == 1:
                iteratio=resultados['idvalor']
                nuevo = 0
        resultados=""
        ident='test'+str(random.randint(10000000, 99999999))
        valores=dict(ident=ident,
            object_identifier=iteratio,
            object_type=dato[1],
            operation="leervalor",datos="")
        producir.putval(topic_name,server_kafka,valores)
        time.sleep(4)
        resultmp=consumir.getval(ident,server_kafka,ident)
        newtopic.delete_topic(ident)
        try:
            resultados=resultmp[0]
        except:
            print("Error Servidor")
            return
        print(resultados)
        salva=str(dato[0])+' '+str(dato[1])+' '+str(resultados)
        g.write( salva + "\n")
    g.close()

