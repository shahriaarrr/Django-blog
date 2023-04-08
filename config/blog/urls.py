from django.urls import path, include
from .views import *

urlpatterns = [
    path('', Index.as_view(), name="index"),
    path('tinymce/', include('tinymce.urls')),
    path('about/', About.as_view(), name='about'),
]
