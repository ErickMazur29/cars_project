from django.db.models.signals import  post_save, post_delete
from django.db.models import Sum
from django.dispatch import receiver
from cars.models import Car, CarInventory


#Função para autalização de inventario de carros
def car_inventory_update():
    cars_count = Car.objects.count() # pega o valor da qtd de carros
    cars_value = Car.objects.aggregate( # pega o valor de todos os carros (preço)
        total_value = Sum('value') # faz a soma
    )['total_value'] # mostra apenas o valor total, não o dicionario

    CarInventory.objects.create( # cria/alimenta o bando de dados do inventario com os novos valores
        cars_count = cars_count,
        cars_value = cars_value
    )



@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    car_inventory_update()


@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
    car_inventory_update()


