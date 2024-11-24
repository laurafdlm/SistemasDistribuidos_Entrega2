"""Authentication service application."""

import logging
import sys
import time
import os
shaold=''
import Ice
import RemoteTypes as rt 

def Clientrt(ic):
    global datos
    global shaold
    adapter = ic.propertyToProxy("remotetypes.Proxy")
    try:
        operador = rt.FactoryPrx.uncheckedCast(adapter)
    except:
        print('Error connexión Proxy')
        time.sleep(3)
        return(1)
    print(operador)
    time.sleep(4)
    tipodato=input('Tipo de datos: (0-Salir,1-Set,2-List,3-Dict)')
    while True:
        try:
            numero=int(tipodato)
        except:
            numero=99
        if numero == 0:
            return(0)
        if numero == 1:
            nombre="Set"
            tiponombre=rt.TypeName.RSet
            menus=['remove','length','contains','hash','add','pop','saveTofile']
            cero=[2,4,6]
            uno=[1,3,5]
            dos=[]
            try:
                rtdatmp=operador.get(tiponombre)
                rtdato=rt.RSetPrx.checkedCast(rtdatmp)
            except:
                print('Error Connexión Servicor')
                time.sleep(3)
                return(1)
            print(type(rtdato))
            break
        if numero == 2:
            nombre="List"
            tiponombre=rt.TypeName.RList
            menus=['remove','length','contains','hash','append','pop','getItem','saveTofile']
            cero=[2,4]
            uno=[1,3,5,6,7]
            dos=[]
            try:
                rtdatmp=operador.get(tiponombre)
                rtdato=rt.RListPrx.checkedCast(rtdatmp)
            except:
                print('Error Connexión Servicor')
                time.sleep(3)
                return(1)
            print(type(rtdato))
            break
        if numero == 3:
            nombre="Dict"
            tiponombre=rt.TypeName.RDict
            menus=['remove','length','contains','hash','setItem','getItem','pop','saveTofile']
            cero=[2,4]
            uno=[1,3,6,7]
            dos=[5]
            try:
                rtdatmp=operador.get(tiponombre)
                rtdato=rt.RDictPrx.checkedCast(rtdatmp)
            except:                                                                 
                print('Error Connexión Servicor')
                time.sleep(3)
                return(1)
            print(type(rtdato))
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
            return(0)    
        while True:
            datos=""
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
            if nombre == "Set":
                valor=""
                if operador == 1:
                    rtdato.remove(msg)
                if operador == 2:
                    valor=rtdato.length()
                if operador == 3:
                    valor=rtdato.contains(msg)
                if operador == 4:
                    valor=rtdato.hash()
                if operador == 5:
                    rtdato.add(msg)
                if operador == 6:
                    valor=rtdato.pop()
                if operador ==7:
                    rtdato.add('9999999999')
                    valor=rtdato.pop()

            if nombre == "List":
                if operador == 1:
                    rtdato.remove(msg)
                if operador == 2:
                    valor=rtdato.length()
                if operador == 3:
                    valor=rtdato.contains(msg)
                if operador == 4:
                    valor=rtdato.hash()
                if operador == 5:
                    rtdato.append(msg)
                    valor=msg
                if operador == 6:
                    try:
                        dat=int(msg)
                    except:
                        print('Error, Necesito el numero de indice')
                        break
                    valor=rtdato.pop(dat)
                if operador == 7:
                    try:
                        dat=int(msg)
                    except:
                        print('Error, Necesito el numero de indice')
                        break
                    valor=rtdato.getItem(dat)
                if operador ==8:
                    valor=rtdato.pop(999999)

            if nombre == "Dict":
                if operador == 1:
                    rtdato.remove(msg)
                if operador == 2:
                    valor=rtdato.length()
                if operador == 3:
                    valor=rtdato.contains(msg)
                if operador == 4:
                    valor=rtdato.hash()
                if operador == 5:
                    rtdato.setItem(msg1,msg2)
                    valor=rtdato.getItem(msg1)
                if operador == 6:
                    valor=rtdato.getItem(msg)
                if operador == 7:
                    valor=rtdato.pop(msg)
                if operador ==8:
                    valor=rtdato.pop('999999')
            print(valor)
            time.sleep(1)
            break

