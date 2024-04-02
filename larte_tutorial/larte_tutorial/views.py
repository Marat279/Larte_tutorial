from django.shortcuts import render


def index(request):
    template = 'larte_tutorial/index.html'
    return render(request, template)
