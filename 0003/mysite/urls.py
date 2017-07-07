from django.conf.urls import url
from mysite.core import views

urlpatterns = [
    url(r'^send/$', views.send, name='send'),
]
