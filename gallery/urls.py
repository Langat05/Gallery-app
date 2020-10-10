from django.urls import path 
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.gallery.static import serve


urlpatterns = [
    path('', views.home),
    path('about/', views.about),
    path('images/', views.images),
    path('search/', views.search),
    path('media/', serve,{'document_root': settings.MEDIA_ROOT}),
    path('static/', serve,{'document_root': settings.STATIC_ROOT}),
    
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)