from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.forward),
    url(r'^search/$', views.index),
    url(r'^search/book/(?P<book_id>\d+)', views.get_book),
]