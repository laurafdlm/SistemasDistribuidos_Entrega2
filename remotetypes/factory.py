"""Needed classes to implement the Factory interface."""
import RemoteTypes as rt  # noqa: F401; pylint: disable=import-error
import Ice
from remotetypes.remotelist import RemoteList
from remotetypes.remoteset import RemoteSet
from remotetypes.remotedict import RemoteDict
from remotetypes.customset import StringSet

class Factory(rt.Factory):
    """Skeleton for the Factory implementation."""
    def get(self,typename,opt1,current: Ice.Current=None)->rt.RTypePrx:
        if typename == rt.TypeName.RDict:
            print("RDict")
            proxy = rt.RDictPrx.uncheckedCast(current.adapter.addWithUUID(RemoteDict(self._nextId)))
            collocProxy = proxy.ice_endpoints([])
            self._nextId=self._nextId+1
            return proxy
        elif typename== rt.TypeName.RList:
            print("RList")
            proxy = rt.RListPrx.uncheckedCast(current.adapter.addWithUUID(RemoteList(self._nextId)))
            collocProxy = proxy.ice_endpoints([])
            self._nextId=self._nextId+1
            return proxy
        else:
            print ("Rset")
            proxy = rt.RSetPrx.uncheckedCast(current.adapter.addWithUUID(RemoteSet(self._nextId)))
            collocProxy = proxy.ice_endpoints([])
            self._nextId=self._nextId+1
            return proxy

    def __init__(self):
        self._nextId = 0


