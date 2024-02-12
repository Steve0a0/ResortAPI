from rest_framework import serializers
from .models import Hotel, Amenity, HotelImage

class AmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenity
        fields = ('__all__')
        
class HotelImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelImage
        fields = ('__all__')
        
class HotelSerializer(serializers.ModelSerializer):
    amenities = AmenitySerializer(many=True, read_only=True) 
    images = HotelImageSerializer(many=True, read_only=True)
    
    main_image = serializers.SerializerMethodField()

    class Meta:
        model = Hotel
        fields = ('__all__') 

    def get_main_image(self, obj):
        request = self.context.get('request')
        image_url = obj.main_image.url 
        return request.build_absolute_uri(image_url)