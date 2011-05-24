from pyramid.events import (
    BeforeRender,
    subscriber ,
    )
from pyramid.renderers import get_renderer

@subscriber(BeforeRender)
def add_site_template(event):
    event['site_template'] = get_renderer('templates/site.pt').implementation()
