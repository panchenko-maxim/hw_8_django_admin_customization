from django.contrib import admin
from .models import AnimalSpecies, AnimalWool, Animal, AnimalAddress


@admin.register(AnimalSpecies)
class AnimalSpeciesAdmin(admin.ModelAdmin):
    fields = ['species']

@admin.register(AnimalWool)
class AnimalWoolAdmin(admin.ModelAdmin):
    fields = ['wool', 'color']

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    fields = ['nickname', 'owner']
