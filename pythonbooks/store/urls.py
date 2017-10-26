from django.conf.urls import url
 
from . import views
 
urlpatterns = [
    url(r'^$', views.save_book, name='save_book'),
 ]