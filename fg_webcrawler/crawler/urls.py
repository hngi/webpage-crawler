from django.urls import path,include
from . import views


urlpatterns = [
    path('', views.index),
    path('/docs', views.documentation),
    path('/downloads', views.downloads)
]
