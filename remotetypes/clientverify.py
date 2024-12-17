"""Authentication service application."""

import logging
import sys
import time
import os
import Ice
import RemoteTypes as rt 

def Clientverify(ic):
    global datos
    global shaold
    adapter = ic.propertyToProxy("remotetypes.Proxy")
    try:
        operador = rt.FactoryPrx.uncheckedCast(adapter)
    except:
        print('Error connexión Proxy')
        time.sleep(3)
        return(0)
    print(operador)
    time.sleep(4)
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
                tiponombre=rt.TypeName.RSet
                try:
                    rtdatmp=operador.get(tiponombre,datmp)
                    rtdato=rt.RSetPrx.checkedCast(rtdatmp)
                except:
                    print('Error Connexión Servidor')
                    time.sleep(3)
                    return(0)
                print(type(rtdato))
                valor=""
                rtdato.add('88888888')
                valor=rtdato.pop()
                salva=dato[0]+' '+dato[1]+' '+valor
                g.write( salva + "\n")
            if dato[1] =="List":
                tiponombre=rt.TypeName.RList
                try:
                    print(dato[2])
                    rtdatmp=operador.get(tiponombre,datmp)
                    rtdato=rt.RListPrx.checkedCast(rtdatmp)
                except:
                    print('Error Connexión Servidor')
                    time.sleep(3)
                    return(0)
                print(type(rtdato))
                valor=""
                valor=rtdato.pop(88888888)
                salva=dato[0]+' '+dato[1]+' '+valor
                g.write( salva + "\n")
            if dato[1] =="Dict":
                tiponombre=rt.TypeName.RDict
                try:
                    rtdatmp=operador.get(tiponombre,datmp)
                    rtdato=rt.RDictPrx.checkedCast(rtdatmp)
                except:
                    print('Error Connexión Servidor')
                    time.sleep(3)
                    return(0)
                print(type(rtdato))
                valor=""
                valor=rtdato.pop('88888888')
                salva=dato[0]+' '+dato[1]+' '+valor
                g.write( salva + "\n")
    f.close()
    g.close()
