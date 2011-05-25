from mortar_rdb import registerSession
from pyramid.config import Configurator
from pyramid.session import (
    UnencryptedCookieSessionFactoryConfig as SessionFactory
    )

from .authentication import SessionAuthenticationPolicy
from .authorization import AuthorizationPolicy

def main(global_config, **settings):
    """
    This function returns a Pyramid WSGI application.
    """
    
    # get secret stuff from files not in source control
    with open(settings['sqlalchemy.url_file']) as source:
        db_url = source.read().strip()
    with open(settings['session.secret_file']) as source:
        secret = source.read().strip()
    
    config = Configurator(
        settings=settings,
        authentication_policy=SessionAuthenticationPolicy(),
        authorization_policy=AuthorizationPolicy(),
        session_factory=SessionFactory(secret),
        )

    registerSession(db_url)

    config.include('pyramid_tm')
    config.scan()
    
    return config.make_wsgi_app()
