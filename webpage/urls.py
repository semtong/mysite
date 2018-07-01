from django.conf.urls import url, include
from django.urls import path
from webpage.views import *

urlpatterns = [
    path('home/', index),
    path('news/', news),
    path('contact/', contact),
    path('about/', about),
    path('test/<year>', test.as_view()),
]
