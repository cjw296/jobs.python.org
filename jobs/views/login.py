from jobs.interfaces import IVelruse
from pyramid.url import resource_url
from pyramid.view import view_config

import logging

@view_config(name='login',
             renderer='templates/login.pt',)
def login(context,request):
    return dict(
        end_point=resource_url(context,request,'loggedin')
        )

@view_config(name='loggedin',
             renderer='templates/loggedin.pt',)
def loggedin(context,request):
    logging.info('velruse info: %r',
                 request.registry.getUtility(IVelruse).query(
            request.POST.get('token')
            ))
    return dict(
        )
