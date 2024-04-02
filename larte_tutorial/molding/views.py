from django.http import HttpResponse


def molding_list(request):
    return HttpResponse('материалы')


def molding_manufacturer(request, manufacturer):
    return HttpResponse(f'автопроизводитель {manufacturer}')


def molding_models(request, manufacturer, models):
    return HttpResponse(f'модель авто: {models}')


def molding_details(request, manufacturer, models, details):
    return HttpResponse(f'деталь {details}')
