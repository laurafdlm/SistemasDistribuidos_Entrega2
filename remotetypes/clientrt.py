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
import random

def Clientrt(topic_name,server_kafka):
    def handler(signum, frame):
        raise TimeoutError("Tiempo límite alcanzado")
    datos=list()
    if os.path.isfile("./datos/registro.bin"):
        with open("./datos/registro.bin","rb") as f:
            registro = pickle.load(f)
    else:
        registro=str(random.randint(10000000, 99999999))
        with open("./datos/registro.bin","wb") as f:
            pickle.dump(registro,f)
    variable=""
    if os.path.isfile("./datos/variables.bin"):
        with open("./datos/variables.bin","rb") as f:
            datos = pickle.load(f)
    else:
        datos=[["nombre","tipo","iteration"]]
    time.sleep(4)
    nueva=1
    msg=""
    msg1=""
    msg2=""
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
            iteratio=i[2]
            nueva=0
    if nueva == 1:
        listdat=['0','1','2','3']
        while True:
            tipodato=input('Tipo de datos: (0-Salir,1-Set,2-List,3-Dict)')
            if tipodato in listdat:
                break
        iteratio=variable + registro
    numero=int(tipodato)
    if numero == 0:
        with open("./datos/variables.bin","wb") as f:
            pickle.dump(datos,f)
        return(0)
    if numero == 1:
        nombre="Set"
        menus=['remove','length','contains','hash','add','pop','leervalor']
        cero=[2,4,6]
        uno=[1,3,5]
        dos=[]
    if numero == 2:
        nombre="List"
        menus=['remove','length','contains','hash','append','pop','getItem','leervalor']
        cero=[2,4]
        uno=[1,3,5,6,7]
        dos=[]
    if numero == 3:
        nombre="Dict"
        menus=['remove','length','contains','hash','setItem','getItem','pop','leervalor']
        cero=[2,4]
        uno=[1,3,6,7]
        dos=[5]

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
        if operador >= contador:
            continue
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
                    valor="leervalor"

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
                    valor="leervalor"

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
                    datvalor=[msg1,msg2]
                if operador == 6:
                    valor="getItem"
                    datvalor=msg
                if operador == 7:
                    valor="pop"
                    datvalor=msg
                if operador ==8:
                    valor="leervalor"

                
            #Funcion get   
#            ident=datetime.today().strftime('%y%m%d%H%M%S%f')
            ident=datetime.today().strftime('%M%S%f')
            datenv=str(datvalor)
            valores=dict(ident=ident,
                        object_identifier=iteratio,
                        object_type=nombre,
                        operation=valor,datos=datenv)
            print(valores)
            resultado=producer.putval(topic_name,server_kafka,valores)
            if resultado==0:
                print("ok")
#            print("\nFlushing records...")
#            producer.flush()
            time.sleep(2)
            resultmp=consumer.getval(ident,server_kafka,ident)
            resultados=resultmp[0]
            try:
                if nueva ==0:
                    for i in datos:
                        if i[0] == variable:
                            i[2]=resultados["idvalor"]
                else:
                    print(resultados['idvalor'])
                    datos.append([variable,nombre,resultados['idvalor']])
                    print(datos)
                print("En la variable {} tipo {} con el ID {} y la función {} el valor optenido es {} es {}".format(variable,nombre,resultados["idvalor"],valor,resultados["result"],resultados["status"]))
            except:
                print("No tengo resultado")
                break
            time.sleep(2)
            break

