from mortar_rdb import getSession
from pyramid.interfaces import IAuthorizationPolicy
from zope.interface import implements

class AuthorizationPolicy(object):

    implements(IAuthorizationPolicy)

    def permits(self, context, principals, permission):
        principal = None
        print principals
        for possible in principals:
            if possible.startswith('system.'):
                continue
            if principal is not None:
                raise ValueError(
                    'Cannot handle multiple principals: %r' % principals
                    )
            principal = possible
        return True
        #role = getSession().query(User.role)\
        #           .filter_by(username=principal).scalar()
        #return role in self.mapping[permission]
    
    def principals_allowed_by_permission(self, context, permission):
        raise NotImplementedError
