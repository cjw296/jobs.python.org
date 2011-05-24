from pyramid.view import view_config

@view_config(renderer='templates/index.pt')
def index(context,request):
    return dict(
        )

