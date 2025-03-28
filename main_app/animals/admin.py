from django.contrib import admin
from .models import AnimalSpecies, AnimalWool, Animal, AnimalAddress


@admin.register(AnimalSpecies)
class AnimalSpeciesAdmin(admin.ModelAdmin):
    fields = ['species']

@admin.register(AnimalWool)
class AnimalWoolAdmin(admin.ModelAdmin):
    fields = ['wool', 'color']

@admin.register(AnimalAddress)
class AnimalAddressAdmin(admin.ModelAdmin):
    pass

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ['nickname', 'animal_species', 'is_vaccinated', 'owner__nickname']
    list_filter = ['is_vaccinated', 'is_tail']
    search_fields = ['nickname', 'owner__nickname']



