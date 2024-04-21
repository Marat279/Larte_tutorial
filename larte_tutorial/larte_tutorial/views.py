from django.shortcuts import render


def index(request):
    template = 'larte_tutorial/index.html'
    context = {
        'title': 'Добро пожаловать в Larte Design',
        'text': 'тут будут списки'
    }
    return render(request, template, context)

