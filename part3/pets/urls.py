from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^home/$', pets_home, name='home'),
    url(r'^home/index/$', pets_index, name='index'),
    url(r'^home/create_owner/$', create_owner, name='create_owner'),
    url(r'^home/create_pet/$', create_pet, name='create_pet'),
]
