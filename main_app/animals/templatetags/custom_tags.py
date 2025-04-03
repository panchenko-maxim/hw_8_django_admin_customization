from django import template
from django.contrib.auth import get_user_model

from animals.models import Animal, AnimalSpecies, AnimalWool

User = get_user_model()

register = template.Library()

@register.filter
def get_animal_info_by_key(item):
    key, value = item
    result_value = None
    if key == "owner":
        try:
            result_value = User.objects.get(id=value).nickname
        except User.DoesNotExist:
            result_value = "Unknown User"
    elif key == "animal_species":
        try:
            result_value = AnimalSpecies.objects.get(id=value)
        except AnimalSpecies.DoesNotExist:
            result_value = "Unknown AnimalSpecies"
    elif key == "animal_wool":
        try:
            result_value = AnimalWool.objects.get(id=value)
        except AnimalWool.DoesNotExist:
            result_value = "Unknown AnimalWool"
    if result_value is not None:
        return f"{key}: {result_value}"
    return f"{key}: {value}"
