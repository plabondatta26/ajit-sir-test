from django.urls import path
from .views import *

urlpatterns = [
    path('', create_writer, name='create_writer'),
    path('writer/list/', writer_list, name='writer_list'),
]
