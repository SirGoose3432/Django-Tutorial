from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^login/$', user_login, name='login'),
    url(r'^logout/$', user_logout, name='logout'),
    url(r'^home/$', pets_home, name='home'),
    url(r'^home/index/$', pets_index, name='index'),
    url(r'^home/user_info/$', user_info, name='user_info'),
    url(r'^home/create_user/$', create_user, name='create_user'),
    url(r'^home/create_owner/$', create_owner, name='create_owner'),
    url(r'^home/create_pet/$', create_pet, name='create_pet'),
]
