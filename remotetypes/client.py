"""Authentication service application."""

import logging
import sys
import time
import os
shaold=''
import Ice
import RemoteTypes as rt 

def Client(ic):
    global datos
    global shaold
    adapter = ic.propertyToProxy("remotetypes.Proxy")
    try:
        identidad = rt.FactoryPrx.uncheckedCast(adapter)
    except:
        print('Error connexión Proxy')
        time.sleep(3)
        quit()
    print(identidad)
    time.sleep(4)
    typename:rt.TypeName.RDict
    print(typename)
    try:
        proxytype=identidad.get(typename)
    except:
        print('Error Usuario')
        time.sleep(3)
        exit(1)
    print(proxytype)
