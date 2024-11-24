"""Needed classes to implement the Factory interface."""
#import pickle
import RemoteTypes as rt  # noqa: F401; pylint: disable=import-error
import Ice
#from fs.osfs import OSFS
from remotetypes.remotelist import RemoteList
from remotetypes.remoteset import RemoteSet
from remotetypes.remotedict import RemoteDict
from remotetypes.iterable import Iterable

class Factory(rt.Factory):
    """Skeleton for the Factory implementation."""
    def get(self,typename,opt1,current: Ice.Current=None)->rt.RTypePrx:
        if typename == rt.TypeName.RSet:
            iteratio=self._iteratio.next()
            if iteratio == '00000000':
                print ('Error max id iteration 200000')
                return
            newiter=int(iteratio)
            proxy = rt.RSetPrx.uncheckedCast(current.adapter.addWithUUID(RemoteSet(newiter)))
            collocProxy = proxy.ice_endpoints([])
            self._nextId=self._nextId+1
            print(type(proxy))
            return proxy
        if typename == rt.TypeName.RList:
            iteratio=self._iteratio.next()
            newiter=int(iteratio)
            proxy = rt.RListPrx.uncheckedCast(current.adapter.addWithUUID(RemoteList(newiter)))
            collocProxy = proxy.ice_endpoints([])
            self._nextId=self._nextId+1
            print(type(proxy))
            return proxy
        if typename == rt.TypeName.RDict:
            iteratio=self._iteratio.next()
            newiter=int(iteratio)
            proxy = rt.RDictPrx.uncheckedCast(current.adapter.addWithUUID(RemoteDict(newiter)))
            collocProxy = proxy.ice_endpoints([])
            self._nextId=self._nextId+1
            print(type(proxy))
            return proxy

    def __init__(self):
        self._nextId = 0
        self._iteratio = Iterable()
