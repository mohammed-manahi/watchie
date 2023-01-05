from django.shortcuts import render


def index(request):
    template = 'account/index.html'
    return render(request, template)
