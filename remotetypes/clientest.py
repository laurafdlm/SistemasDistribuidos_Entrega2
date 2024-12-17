"""Authentication service application."""

import logging
import sys
import time
import os
import Ice
import RemoteTypes as rt 

def Clientest(ic):
    g=open("./datos/resultado.txt","w+")
    datlist=list()
    adapter = ic.propertyToProxy("remotetypes.Proxy")
    try:
        operador = rt.FactoryPrx.uncheckedCast(adapter)
    except:
        print('Error connexión Proxy')
        time.sleep(3)
        return(0)
    print(operador)
    time.sleep(4)
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
                tiponombre=rt.TypeName.RSet
                try:
                    rtdatmp=operador.get(tiponombre,"")
                    rtdato=rt.RSetPrx.checkedCast(rtdatmp)
                except:
                    print('Error Connexión Servidor')
                    time.sleep(3)
                    return(1)
                print(type(rtdato))
                valor=""
                for i in datmp.split(','):
                    rtdato.add(str(i))
                rtdato.add('99999999')
                valor=rtdato.pop()
                salva=dato[0]+' '+dato[1]+' '+valor
                g.write( salva + "\n")
            if dato[1] =="List":
                valor=list(datmp.split(','))
                print (valor)
                print(type(valor))
                tiponombre=rt.TypeName.RList
                try:
                    rtdatmp=operador.get(tiponombre,"")
                    rtdato=rt.RListPrx.checkedCast(rtdatmp)
                except:
                    print('Error Connexión Servidor')
                    time.sleep(3)
                    return(1)
                print(type(rtdato))
                for i in datmp.split(','):
                    rtdato.append(str(i))
                valor=rtdato.pop(99999999)
                salva=dato[0]+' '+dato[1]+' '+valor
                g.write( salva + "\n")
            if dato[1] =="Dict":
                valor=dict(item.split(':')
                for item in datmp.split(','))
                print (valor)
                print(type(valor))
                tiponombre=rt.TypeName.RDict
                try:
                    rtdatmp=operador.get(tiponombre,"")
                    rtdato=rt.RDictPrx.checkedCast(rtdatmp)
                except:
                    print('Error Connexión Servidor')
                    time.sleep(3)
                    return(1)
                print(type(rtdato))
                for i in datmp.split(','):
                    j=i.split(':')
                    rtdato.setItem(str(j[0]),str(j[1]))
                valor=rtdato.pop('99999999')
                salva=dato[0]+' '+dato[1]+' '+valor
                g.write( salva + "\n")
    f.close()
    g.close()

