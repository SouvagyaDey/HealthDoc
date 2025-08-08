from django.urls import path
from .views import doctor_list

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', doctor_list, name='doctor_list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)