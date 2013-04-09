from zope.interface import Interface

class IVelruse(Interface):
    """
    An interface for looking up a Velruse token the
    current Velruse store.
    """

    def query(token):
        """
        Return the information provided by Velruse for
        the supplied token, raise an exception in the
        token is not valid. 
        """
