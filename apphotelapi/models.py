from django.db import models

class Amenity(models.Model):
    name = models.CharField(max_length=100,null=True, blank=True)
    
    def __str__(self):
        return self.name

class HotelImage(models.Model):
    image = models.ImageField(upload_to='hotel_images/')
    
    def __str__(self):
        return str(self.image)

class Hotel(models.Model):
    hotel_name = models.CharField(max_length=100,null=True, blank=True)
    hotel_area = models.CharField(max_length=100, null=True, blank=True)
    hotel_beds = models.PositiveSmallIntegerField()
    hotel_accommodates = models.PositiveSmallIntegerField(null=True, blank=True)
    hotel_star_rating = models.PositiveSmallIntegerField(default=0)
    hotel_description = models.TextField(null=True, blank=True)
    hotel_amenities= models.ManyToManyField(Amenity)
    hotel_price = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True)
    main_hotel_image = models.ImageField(upload_to='hotel_images/')
    images = models.ManyToManyField(HotelImage)
    latitude=models.CharField(max_length=100, null=True, blank=True)
    longitude=models.CharField(max_length=100, null=True, blank=True)
    
    def generate_star_rating_html(self):
        full_stars = self.hotel_star_rating
        empty_stars = 5 - full_stars  # Assuming a maximum of 5 stars

        full_star_html = '★' * full_stars  # ★ is a star character
        empty_star_html = '☆' * empty_stars  # ☆ is an empty star character

        star_rating_html = f'{full_star_html}{empty_star_html}'
        return star_rating_html

    def __str__(self):
        return self.hotel_name