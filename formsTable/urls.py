from django.conf.urls import url
from formsTable import views

urlpatterns = [url(r'^$', views.index, name='index'),]