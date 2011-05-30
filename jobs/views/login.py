from pyramid.view import view_config

@view_config(name='login',
             renderer='templates/login.pt',)
def login(context,request):
    return dict(
        )

@view_config(name='loggedin',
             renderer='templates/loggedin.pt',)
def loggedin(context,request):
    print "LOGGED IN!"
    return dict(
        )
