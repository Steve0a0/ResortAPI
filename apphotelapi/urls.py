from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('amenities/', views.list_amenities, name='list_amenities'),
    path('hotels/', views.list_hotels, name='list_hotels'),
    path('hotels/<int:id>/images/', views.list_hotel_images, name='list_hotel_images'),
    path('', views.hotel_list, name='hotel_list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)