from pyramid.view import view_config

@view_config(renderer='templates/index.pt')
def index(context,request):
    return dict(
        )

@view_config(name='secure_index',
             renderer='templates/secure_index.pt',
             permission='authenticated')
def secure_index(context,request):
    return dict(
        )

