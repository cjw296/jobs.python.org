from logging import getLogger
from pyramid.exceptions import NotFound
from pyramid.httpexceptions import HTTPNotFound
from pyramid.httpexceptions import HTTPInternalServerError
from pyramid.view import view_config
from traceback import format_exc

logger = getLogger()

@view_config(context=NotFound)
def notfound_view(context,request):
    message = '404 NotFound: '+request.path
    logger.info(message)
    return HTTPNotFound(body=message)

@view_config(context=Exception)
def error_view(context,request):
    logger.exception('500 Error: '+request.path)
    return HTTPInternalServerError(body='500 Error:\n'+format_exc())

