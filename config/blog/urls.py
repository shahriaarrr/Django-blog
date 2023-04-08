from django.urls import path, include
from .views import *

urlpatterns = [
    path('', Index.as_view(), name="index"),
    path('tinymce/', include('tinymce.urls')),
    path('about/', About.as_view(), name='about'),
    path('<int:pk>/', DetailArticleView.as_view(), name='detail_article'),
    path('<int:pk>/like/', LikeArticle.as_view(), name='like_article'),
    path('featured/', Featured.as_view(), name='ّfeatured'),
]
