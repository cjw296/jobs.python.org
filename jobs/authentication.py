from pyramid.interfaces import IAuthenticationPolicy
from pyramid.security import Authenticated
from pyramid.security import Everyone
from zope.interface import implements

class SessionAuthenticationPolicy(object):

    implements(IAuthenticationPolicy)

    def __init__(self,user_key='user_id'):
        self.user_key = 'user_id'
    
    def authenticated_userid(self, request):
        return request.session.get(self.user_key)

    def effective_principals(self, request):
        principals = [Everyone]
        user_id = self.authenticated_userid(request)
        if user_id is not None:
            principals.append(Authenticated)
            principals.append(user_id)

        return principals

    def remember(self, request, principal, **kw):
        request.session[self.user_key]=principal
        return []

    def forget(self, request):
        if self.user_key in request.session:
            del request.session[self.user_key]
        return []
