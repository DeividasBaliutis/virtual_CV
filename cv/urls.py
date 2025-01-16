from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('experience/', views.experience, name='experience'),
    path('hobbies/', views.hobbies_view, name='hobbies'),
    path('contacts/', views.contacts, name='contacts'),
    path('i18n/', include('django.conf.urls.i18n')),
    path('download/', views.download_cv, name='download_cv'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
