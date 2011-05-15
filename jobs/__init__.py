from mortar_rdb import registerSession, getSession
from pyramid.config import Configurator

import logging

logger = logging.getLogger()

def main(global_config, **settings):
    """
    This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    
    config.scan()
    
    return config.make_wsgi_app()
