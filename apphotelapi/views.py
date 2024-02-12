
from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import Amenity, Hotel, HotelImage

def list_amenities(request):
    amenities = Amenity.objects.all()
    data = [{'id': amenity.id, 'name': amenity.name} for amenity in amenities]
    return JsonResponse(data, safe=False)

def list_hotels(request):
    hotels = Hotel.objects.all()
    data = []
    for hotel in hotels:
        amenities = list(hotel.hotel_amenities.all().values_list('name', flat=True))
        images = list(hotel.images.all().values_list('image', flat=True))
        hotel_data = {
            'id': hotel.id,
            'name': hotel.hotel_name,
            'Area': hotel.hotel_area,
            'Beds': hotel.hotel_beds,
            'Accommodates': hotel.hotel_accommodates,
            'star': hotel.hotel_star_rating,
            'Description': hotel.hotel_description,
            'Amenities': amenities,
            'Price': hotel.hotel_price,
            'MainImage': hotel.main_hotel_image.url if hotel.main_hotel_image else None,
            'Images': images,
            'Latitude': hotel.latitude,
            'Longitude': hotel.longitude
        }
        data.append(hotel_data)
    return JsonResponse(data, safe=False)


def list_hotel_images(request, id):
    hotel_images = HotelImage.objects.filter(id=id)
    data = [{'id': image.id, 'image_url': image.image.url} for image in hotel_images]
    return JsonResponse(data, safe=False)


def hotel_list(request):
    hotels = Hotel.objects.all()
    return render(request, 'hotel_list.html', {'hotels': hotels})

# views.py

from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Amenity, Hotel, HotelImage

# Other view functions...

def add_hotel(request):
    if request.method == 'POST':
        # Retrieve form data
        hotel_name = request.POST.get('hotel-name')
        hotel_area = request.POST.get('hotel-area')
        hotel_beds = request.POST.get('hotel-beds')
        hotel_accommodates = request.POST.get('hotel-accommodates')
        hotel_star_rating = request.POST.get('hotel-star-rating')
        hotel_description = request.POST.get('hotel-description')
        hotel_price = request.POST.get('hotel-price')
        main_hotel_image = request.FILES.get('hotel-main-image')
        additional_images = request.FILES.getlist('hotel-images')
        amenities = request.POST.getlist('hotel-amenities')
        latitude = request.POST.get('hotel-latitude')
        longitude = request.POST.get('hotel-longitude')
        
        try:
            # Create Hotel object and save to database
            hotel = Hotel.objects.create(
                hotel_name=hotel_name,
                hotel_area=hotel_area,
                hotel_beds=hotel_beds,
                hotel_accommodates=hotel_accommodates,
                hotel_star_rating=hotel_star_rating,
                hotel_description=hotel_description,
                hotel_price=hotel_price,
                main_hotel_image=main_hotel_image,
                latitude=latitude,
                longitude=longitude
            )
            
            # Save additional images
            for image in additional_images:
                hotel_image = HotelImage.objects.create(image=image)
                hotel.images.add(hotel_image)
            
            # Save amenities
            for amenity in amenities:
                amenity_obj, created = Amenity.objects.get_or_create(name=amenity)
                hotel.hotel_amenities.add(amenity_obj)
            
            # Redirect to a success page or some other page
            return redirect('hotel_list')  
        except Exception as e:
            # Handle any errors that occur during the creation and saving of the hotel object
            print(f"An error occurred: {e}")
            # Optionally, you can return an error response or render a specific template for error handling
            return render(request, 'error.html', {'error_message': 'An error occurred while adding the hotel.'})

# Other view functions...
