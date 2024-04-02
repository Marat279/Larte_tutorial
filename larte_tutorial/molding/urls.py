from django.urls import path
from . import views


urlpatterns = [
    path('', views.molding_list),
    path('<str:manufacturer>/', views.molding_manufacturer),
    path('<str:manufacturer>/<str:models>/', views.molding_models),
    path('<str:manufacturer>/<str:models>/<str:details>/',
         views.molding_details),
]
