from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('molding/', include('molding.urls', namespace='molding')),
]
