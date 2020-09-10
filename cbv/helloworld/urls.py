from helloworld import views
from django.urls import include, path
from django.conf.urls import url

app_name = 'helloworld'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
]

