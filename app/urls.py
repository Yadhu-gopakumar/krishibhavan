from . import views
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),  # Home view
    path('weather/', views.weather, name='weather'),  # Weather view
    path('about/', views.about, name='about'),  # About view
    path('ecart/', views.ecart, name='ecart'),  # Ecart view
    path('marketrate/', views.marketrate, name='marketrate'),
    path('plantingmaterials/', views.plantingmaterials, name='plantingmaterials'),
    path('tips/', views.tips, name='tips'),  # Tips view
    path('gallery/', views.gallery, name='gallery'),  # Gallery view
    path('contact/', views.contact, name='contact'),  # Contact view
    
]
static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  # Serve static files in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Serve media files in