from mortar_rdb import registerSession
from pyramid.config import Configurator
from pyramid.session import (
    UnencryptedCookieSessionFactoryConfig as SessionFactory
    )
from pyramid.wsgi import wsgiapp2
from velruse.app import make_app as make_velruse_app

from .authentication import SessionAuthenticationPolicy
from .authorization import AuthorizationPolicy
from .utilities import DirectAccess

def main(global_config, **settings):
    """
    This function returns a Pyramid WSGI application.
    """
    
    # get secret stuff from files not in source control
    with open(settings['sqlalchemy.url_file']) as source:
        db_url = source.read().strip()
    with open(settings['session.secret_file']) as source:
        secret = source.read().strip()

    # set up config
    config = Configurator(
        settings=settings,
        authentication_policy=SessionAuthenticationPolicy(),
        authorization_policy=AuthorizationPolicy(),
        session_factory=SessionFactory(secret),
        )

    # set up database
    registerSession(db_url)

    # setup velruse
    velruse = make_velruse_app(settings['velruse_config_file'])
    velruse.__name__='velruse'
    config.registry.registerUtility(DirectAccess(velruse))
    config.add_view(wsgiapp2(velruse), name='velruse')

    # set up transactions
    config.include('pyramid_tm')

    # static views
    config.add_static_view('static','jobs:static')
    config.add_static_view('favicon.ico',
                           'jobs:static/favicon.ico')
    
    # scan for everything else
    config.scan()
    
    return config.make_wsgi_app()
