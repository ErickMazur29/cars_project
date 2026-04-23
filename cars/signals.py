from django.db.models.signals import pre_save, post_save, pre_delete, post_delete
from django.dispatch import receiver
from cars.models import Car

@receiver(pre_save, sender=Car)
def car_pre_save(sender, instance, **kwargs):
    print('### PRE SAVE REALIZED ###')

@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    print('### POST SAVE REALIZED ###')

@receiver(pre_delete, sender=Car)
def car_pre_delete(sender, instance, **kwargs):
    print('### PRE DELETE REALIZED ###')

@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
    print('### POST DELETE REALIZED ###')


