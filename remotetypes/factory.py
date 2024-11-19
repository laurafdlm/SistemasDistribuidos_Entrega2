"""Needed classes to implement the Factory interface."""
#import pickle
import RemoteTypes as rt  # noqa: F401; pylint: disable=import-error
import Ice
#from fs.osfs import OSFS
from remotetypes.remotelist import RemoteList
from remotetypes.remoteset import RemoteSet
from remotetypes.remotedict import RemoteDict

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
            proxy.add("jose")
            return proxy

    def __init__(self):
#        self.home_fs = OSFS('./')
        self._nextId = 0
#        if not self.home_fs.exists('/datos'):
#            self.home_fs.makedirs('/datos')
#        self.pathfs=self.home_fs.getsyspath("/datos/")



