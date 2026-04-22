from django.shortcuts import render
from cars.models import Car
from cars.forms import CarModelForm
from django.views.generic import ListView, CreateView, DetailView

def index(request):
    return render(request, 'index.html')


#Gera lista de carros no cars.html e faz a função de busca
class CarsListView(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'

    def get_queryset(self):
        cars = super().get_queryset().order_by('brand')
        search = self.request.GET.get('search')

        if search:
            cars = cars.filter(model__icontains = search)
        return cars

#Faz o formulario e gera seus registros
class NewCarCreateView(CreateView):
    model = Car
    form_class = CarModelForm
    template_name = 'new_car.html'
    success_url = '/cars/'
        

#Gera pagina de detalhes de cada carro
class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'