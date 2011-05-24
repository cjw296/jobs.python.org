from mortar_rdb import registerSession
from pyramid.config import Configurator

import logging

logger = logging.getLogger()

def main(global_config, **settings):
    """
    This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)

    with open(settings['sqlalchemy.url_file']) as db_url:
        registerSession(db_url.read().strip())
    
    config.scan()
    
    return config.make_wsgi_app()
