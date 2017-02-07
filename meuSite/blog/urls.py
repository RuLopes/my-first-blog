from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.post_list),
    url(r'^novo/$',views.novo),
    url(r'^index/$',views.index),
]
