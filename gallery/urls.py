from django.urls import path 
from gallery.views import images,about,home,search_category
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', home),
    path('about/', about),
    path('images/', images),
    path('search_category/', search_category),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)