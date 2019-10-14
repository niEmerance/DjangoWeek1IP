from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$', views.gallery,name='gallery'),
    url(r'^search/', views.searchImage, name='searchImage'),
    url(r'^description/(\d+)',views.imgDesc,name='imgDesc')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)