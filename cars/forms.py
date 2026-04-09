from django import forms
from cars.models import Brand

class CarForm(forms.Form):
    model = forms.CharField(max_length=200)
    brand = forms.ModelChoiceField(Brand.objects.all())
    model_year = forms.IntegerField()
    factory_year = forms.IntegerField()
    plate = forms.IntegerField(max_value=10)
    photo = forms.ImageField()
    value = forms.IntegerField()
