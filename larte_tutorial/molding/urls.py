from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('molding/', views.molding_list),
    path('molding/<str:manufacturer>/', views.molding_manufacturer),
    path('molding/<str:manufacturer>/<str:models>/', views.molding_models),
    path('molding/<str:manufacturer>/<str:models>/<str:details>/',
         views.molding_details),
]
