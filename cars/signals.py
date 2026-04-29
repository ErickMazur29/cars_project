from django.db.models.signals import  post_save, post_delete, pre_save
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


@receiver(pre_save, sender=Car)
def car_pre_save(sender, instance, **kwargs):
    if not instance.bio:
        instance.bio = (
            f"O {instance.brand.name} {instance.model}, ano modelo {instance.model_year} "
            f"(fabricado em {instance.factory_year}), é uma excelente opção para quem busca "
            f"conforto, desempenho e confiabilidade no dia a dia. "
            f"Este veículo encontra-se em ótimo estado de conservação, pronto para uso, "
            f"atendendo bem tanto às necessidades urbanas quanto a viagens. "
            f"Placa {instance.plate}. Disponível pelo valor de R$ {instance.value:,.2f}, "
            f"representando uma ótima oportunidade."
        )

@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    car_inventory_update()


@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
    car_inventory_update()


