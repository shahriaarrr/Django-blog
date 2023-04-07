from django.urls import path
from .views import *

urlpatterns = [
    path('', Index.as_view(), name="index"),
    path('about/', About.as_view(), name='about'),
]
