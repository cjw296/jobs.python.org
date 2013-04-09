# Wrapper(s) for accessing Velruse in different ways
from zope.interface import implements

from .interfaces import IVelruse

class DirectAccess:

    implements(IVelruse)

    def __init__(self,sessionmiddleware):
        self.velruse = sessionmiddleware.wrap_app

    def query(self,token):
        return self.velruse.store.retrieve(token)

