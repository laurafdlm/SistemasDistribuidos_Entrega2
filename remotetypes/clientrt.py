"""Authentication service application."""

import logging
import sys
import time
import os
shaold=''
import Ice
import RemoteTypes as rt 
class FuncDict:
    def remove(msg):
        rtdato.remove(msg)
    def length():
        return rtdato.length()
    def contains(msg):
        return rtdato.contains(msg)
    def hash():
        return rtdato.hash()
    def setItem(msg1,msg2):
        rtdato.setItem({msg1:msg2})
    def getItem(msg):
        return rtdato.getItem(msg)
    def pop(msg):
        return rtdato.pop(msg)

class FuncList:
    def remove(msg):
        rtdato.remove(msg)
    def length():
        return rtdato.length()
    def contains(msg):
        return rtdato.contains(msg)
    def hash():
        return rtdato.hash()
    def append(msg):
        rtdato.append(msg)
    def pop(msg):
        return rtdato.pop(msg)
    def getItem(msg):
        return rtdato.getItem(msg)

class FuncSet:
    def remove(msg):
        rtdato.remove(msg)
    def length():
        return rtdato.length()
    def contains(msg):
        return rtdato.contains(msg)
    def hash():
        return rtdato.hash()
    def add(msg):
        rtdato.add(msg)
    def pop():
        return rtdato.pop()

def Clientrt(ic):
    global datos
    global shaold
    adapter = ic.propertyToProxy("remotetypes.Proxy")
    try:
        operador = rt.FactoryPrx.uncheckedCast(adapter)
    except:
        print('Error connexión Proxy')
        time.sleep(3)
        quit
    print(operador)
    time.sleep(4)
    tipodato=input('Tipo de datos: (0-Salir,1-Set,2-List,3-Dict)')
    while True:
        try:
            numero=int(tipodato)
        except:
            numero=99
        if numero == 0:
            quit()
        if numero == 1:
            nombre="Set"
            tiponombre=rt.TypeName.RSet
            menus=['remove','length','contains','hash','add','pop']
            cero=[2,4,6]
            uno=[1,3,5]
            dos=[]
            break
        if numero == 2:
            nombre="List"
            tiponombre=rt.TypeName.RList
            menus=['remove','length','contains','hash','append','pop','getItem']
            cero=[2,4]
            uno=[1,3,5,6,7]
            dos=[]
            break
        if numero == 3:
            nombre="Dict"
            tiponombre=rt.TypeName.RDict
            menus=['remove','length','contains','hash','setItem','getItem','pop']
            cero=[2,4]
            uno=[1,3,6,7]
            dos=[5]
            break
    while True:
        try:
            proxytype=operador.get(tiponombre)
        except:
            print('Error Connexión Servicor')
            time.sleep(3)
            exit(1)
        print(proxytype)
        contador=1
        for i in menus:
            print(contador,' Si quieres ejecutar la función: ',i)
            contador +=1
        print ( '0 Salir')
        valor= input('Entra el numero de opción: (0-{})'.format(contador -1))
        try:
            numero=int(valor)
        except:
            numero=99
        if numero == 0:
            quit()
        if numero in range(1,len(menus)):
            try:
                rtdato=operador.get(tiponombre)
            except:
                print('Error Connexión Servicor')
                time.sleep(3)
                exit(1)
            print(rtdato)
            while True:
                datos=""
                if numero in cero:
                    if nombre == "Dict":
                        valor=getattr(FuncDict, menus[numero-1])()
                    elif nombre=="List":
                        valor=getattr(FuncList, menus[numero-1])()
                    elif nombre=="Set":
                        valor=getattr(FuncSet, menus[numero-1])()
                    print(valor)
                    time.sleep(1)
                    break
                elif numero in uno:
                    dattmp=input('Introduce el valor o key necesario(Solo caracteres)')
                    try:
                        datos=str(dattmp)
                    except:
                        continue
                    valor=""
                    if nombre=="Dict":
                       valor=getattr(FuncDict, menus[numero-1])(datos)
                    elif nombre=="List":
                        valor=getattr(FuncList, menus[numero-1])(datos)
                    elif nombre=="Set":
                        print(rtdato)
                        print(type(rtdato))
                        valor=rtdato.contains(datos)
#                        valor=getattr(FuncSet, menus[numero-1])(datos)
                    print(valor)
                    time.sleep(1)
                    break
                elif numero in dos:
                    datkey=input('Introduce la key del Dict(Solo caracteres)')
                    datvalue=input('Introduce el valor del Dict(Solo caracteres)')
                    try:
                        dickey=str(datkey)
                        dicvalue=str(datvalue)
                    except:
                        continue
                    valor=getattr(FuncDict, menus[numero-1])(dickey,dicvalue)
                    print(valor)
                    time.sleep(1)
                    break

