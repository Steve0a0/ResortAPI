from django.contrib import admin
from .models import Amenity, HotelImage,Hotel
# Register your models here.

admin.site.register(Amenity)
admin.site.register(HotelImage)
admin.site.register(Hotel)