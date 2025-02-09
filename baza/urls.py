from django.urls import path
from django.views.generic import detail

from .views import index,about
urlpatterns = [
    path('', index, name='index'),
    path('', about, name='about'),

]