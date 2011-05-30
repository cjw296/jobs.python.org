from pyramid.events import (
    BeforeRender,
    subscriber ,
    )
from pyramid.renderers import get_renderer
from pyramid.security import authenticated_userid

@subscriber(BeforeRender)
def add_site_template(event):
    request = event['request']
    
    event['site_template'] = get_renderer('templates/site.pt').implementation()

    event['user_id'] = authenticated_userid(request)
