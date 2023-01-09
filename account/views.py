from django.shortcuts import render
from account.forms import RegisterForm
from django.contrib.auth.decorators import login_required


def index(request):
    """
    Create index view
    :param request:
    :return index template:
    """
    template = 'account/index.html'
    return render(request, template)


@login_required
def dashboard(request):
    """
    Create user dashboard view
    :param request:
    :return dashboard template:
    """
    template = 'account/dashboard.html'
    return render(request, template)
