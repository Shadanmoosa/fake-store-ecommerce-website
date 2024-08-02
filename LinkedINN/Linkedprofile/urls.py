from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # home section
    path('', views.loading),
    path('home', views.home),
    path('mens', views.mens),
    path('women', views.women),
    path('jewelery', views.jewelery),
    path('electronics', views.electronics),
    path('productdetails/<int:ids>',views.productdetails),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)