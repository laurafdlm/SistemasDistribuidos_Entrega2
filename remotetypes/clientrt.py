"""Authentication service application."""

import logging
import sys
import time
import os
shaold=''
import pickle
from remotetypes.json_server import JsonProducer
from remotetypes.json_client import JsonConsumer
from datetime import datetime

def Clientrt():
    datos=list()
    variable=""
    if os.path.isfile("./datos/variables.bin"):
        with open("./datos/variables.bin","rb") as f:
            datos = pickle.load(f)
    else:
        datos=[["nombre","tipo","iteration"]]
    global shaold
    time.sleep(4)
    nueva=1
    producer=JsonProducer()
    consumer=JsonConsumer()
    variable=input('Introduce el nombre de la variable()')
    for i in datos:
        if i[0] == variable:
            if i[1] == "Set":
                tipodato="1"
            elif i[1] == 'List':
                tipodato="2"
            else:
                tipodato="3"
            iteration=i[2]
            nueva=0
    if nueva == 1:
        tipodato=input('Tipo de datos: (0-Salir,1-Set,2-List,3-Dict)')
        iteration=""

    while True:
        try:
            numero=int(tipodato)
        except:
            numero=0
        if numero == 0:
            with open("./datos/variables.bin","wb") as f:
                pickle.dump(datos,f)
            return(0)
        if numero == 1:
            nombre="Set"
            menus=['remove','length','contains','hash','add','pop','savetofile']
            cero=[2,4,6]
            uno=[1,3,5]
            dos=[]
            break
        if numero == 2:
            nombre="List"
            menus=['remove','length','contains','hash','append','pop','getItem','savetofile']
            cero=[2,4]
            uno=[1,3,5,6,7]
            dos=[]
            break
        if numero == 3:
            nombre="Dict"
            menus=['remove','length','contains','hash','setItem','getItem','pop','savetofile']
            cero=[2,4]
            uno=[1,3,6,7]
            dos=[5]
            break

    while True:
        contador=1
        for i in menus:
            print(contador,' Si quieres ejecutar la función: ',i)
            contador +=1
        print ( '0 Salir')
        valor= input('Entra el numero de opción: (0-{})'.format(contador -1))
        try:
            operador=int(valor)
        except:
            operador=99
        if operador == 0:
            with open("./datos/variables.bin","wb") as f:
                pickle.dump(datos,f)
            return(0)    
        while True:
            if operador in uno:
                dattmp=input('Introduce el valor o key necesario(Solo caracteres)')
                try:
                    msg=str(dattmp)
                except:
                    print('Valor no valido')
                    continue
                if msg == "":
                    break
            if operador in dos:
                datkey=input('Introduce la key del Dict(Solo caracteres)')
                datvalue=input('Introduce el valor del Dict(Solo caracteres)')
                try:
                    msg1=str(datkey)
                    msg2=str(datvalue)
                except:
                    print('Valores no validos')
                    continue
                if msg1 == "":
                    break
            valor=""
            resultado=""
            datvalor=""
            datvalor2=""
            if nombre == "Set":
                if operador == 1:
                    valor="remove"
                    datvalor=msg
                if operador == 2:
                    valor="length"
                if operador == 3:
                    valor="contains"
                    datvalor=msg
                if operador == 4:
                    valor="hash"
                if operador == 5:
                    valor="add"
                    datvalor=msg
                if operador == 6:
                    valor="pop"
                if operador ==7:
                    valor="savetofile"

            if nombre == "List":
                if operador == 1:
                    valor="remove"
                if operador == 2:
                    valor="length"
                if operador == 3:
                    valor="contains"
                    datvalor=msg
                if operador == 4:
                    valor="hash"
                if operador == 5:
                    valor="append"
                    datvalor=msg
                if operador == 6:
                    try:
                        dat=int(msg)
                    except:
                        print('Error, Necesito el numero de indice')
                        break
                    valor="pop"
                    datvalor=dat
                if operador == 7:
                    try:
                        dat=int(msg)
                    except:
                        print('Error, Necesito el numero de indice')
                        break
                    valor="getItem"
                    datvalor=dat
                if operador ==8:
                    valor="savetofile"

            if nombre == "Dict":
                if operador == 1:
                    valor="remove"
                    datvalor=msg
                if operador == 2:
                    valor="length"
                if operador == 3:
                    valor="contains"
                    datvalor=msg
                if operador == 4:
                    valor="hash"
                if operador == 5:
                    valor="setItem"
                    datvalor=msg1
                    datvalor2=msg2
                if operador == 6:
                    valor="getItem"
                    datvalor=msg
                if operador == 7:
                    valor="pop"
                    datvalor=msg
                if operador ==8:
                    valor="savetofile"
            #Funcion get   
            ident=datetime.today().strftime('%y%m%d%H%M%S%f')
            if valor=="setItem":
                datenv=dict(datvalor:datvalor2)
            else:
                datenv=list(datvalor)
            valores=dict(ident=ident,
                        object_identifier=iteration,
                        object_type=nombre,
                        operation=valor,datos=datvalor)


            producer.putoperation("mi_pruebas10",valores)
            time.sleep(2)
            resultados=consumer.get(ident)
            if nueva ==0:
                for i in datos:
                    if i[0] == variable:
                        i[2]=resultados["idvalor"]
            else:
                datos.append([variable,nombre,resultados["idvalor"]])
            print("En la variable {} tipo {} con el ID {} y la función {} el valor optenido es {} es {}".format(variable,nombre,resultados["idvalor"],valor,resultados["result"],resultados["status"])
            time.sleep(2)
            break

