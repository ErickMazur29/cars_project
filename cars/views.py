from django.shortcuts import render
from cars.models import Car
from django.urls import reverse_lazy
from cars.forms import CarModelForm
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


#Pagina inicial
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


#Gera pagina de detalhes de cada carro
class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'


#Faz o formulario e gera seus registros + requisição de login
@method_decorator(login_required(login_url='login'), name='dispatch')
class NewCarCreateView(CreateView):
    model = Car
    form_class = CarModelForm
    template_name = 'new_car.html'
    success_url = '/cars/'


#Editar carro especifico + requisição de login
@method_decorator(login_required(login_url='login'), name='dispatch')
class CarUpdateView(UpdateView):
    model = Car
    form_class = CarModelForm
    template_name = 'car_update.html'
    context_object_name = 'car'
    success_url = '/cars/'

    def get_success_url(self):
        return reverse_lazy('car_detail', kwargs={'pk': self.object.pk})


#Deletar carro + requisição de login
@method_decorator(login_required(login_url='login'), name='dispatch')
class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car_delete.html'
    context_object_name = 'car'
    success_url = '/cars/'