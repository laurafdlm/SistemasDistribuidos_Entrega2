"""Needed classes to implement the Factory interface."""
#import pickle
import RemoteTypes as rt  # noqa: F401; pylint: disable=import-error
import Ice
#from fs.osfs import OSFS
from remotetypes.remotelist import RemoteList
from remotetypes.remoteset import RemoteSet
from remotetypes.remotedict import RemoteDict
from remotetypes.iterable import Iterable
import os.path

class Factory(rt.Factory):
    """Skeleton for the Factory implementation."""
    def get(self,typename,opt1,current: Ice.Current=None)->rt.RTypePrx:
        if typename == rt.TypeName.RSet:
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
                return
            print(iteratio)
            newiter=int(iteratio)
            proxy = rt.RSetPrx.uncheckedCast(current.adapter.addWithUUID(RemoteSet(newiter)))
            collocProxy = proxy.ice_endpoints([])
            self._nextId=self._nextId+1
            print(type(proxy))
            return proxy
        if typename == rt.TypeName.RList:
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
                return
            newiter=int(iteratio)
            proxy = rt.RListPrx.uncheckedCast(current.adapter.addWithUUID(RemoteList(newiter)))
            collocProxy = proxy.ice_endpoints([])
            self._nextId=self._nextId+1
            print(type(proxy))
            return proxy
        if typename == rt.TypeName.RDict:
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
                return
            newiter=int(iteratio)
            proxy = rt.RDictPrx.uncheckedCast(current.adapter.addWithUUID(RemoteDict(newiter)))
            collocProxy = proxy.ice_endpoints([])
            self._nextId=self._nextId+1
            print(type(proxy))
            return proxy

    def __init__(self):
        self._nextId = 0
        self._iteratio = Iterable()
