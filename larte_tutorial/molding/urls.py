from django.urls import path
from . import views

app_name = 'molding'

urlpatterns = [
    path('', views.molding_list, name='moldings'),
    path('<str:manufacturer>/', views.molding_manufacturer,
         name='manufacturer'),
    path('<str:manufacturer>/<str:models>/', views.molding_models,
         name='model'),
    path('<str:manufacturer>/<str:models>/<str:details>/',
         views.molding_details, name='details'),
]
