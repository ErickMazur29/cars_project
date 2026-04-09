from django.shortcuts import render
from cars.models import Car
# Create your views here.

def car_view(request):
    cars = Car.objects.all().order_by('model_year')
    search = request.GET.get('search')
    if search:
        cars = Car.objects.filter(model__icontains = search)

    return render(
        request, 
        'cars.html',
        {'cars' : cars}
    )

def index(request):
    return render(request, 'index.html')
