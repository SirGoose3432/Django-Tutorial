from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^index/$', pets_index, name='index'),
    url(r'^home/$', pets_home, name='home'),
]