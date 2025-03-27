from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class AnimalSpecies(models.Model):
    species = models.CharField(max_length=100, blank=True, verbose_name='species')


class AnimalWool(models.Model):
    wool = models.BooleanField(default=False, verbose_name='wool')
    color = models.CharField(max_length=50, verbose_name='color')


class Animal(models.Model):
    owner = models.ForeignKey(User, blank=True, on_delete=models.DO_NOTHING, related_name='owner')
    animal_species = models.ForeignKey(AnimalSpecies, on_delete=models.DO_NOTHING, related_name='animal_species')
    animal_wool = models.ForeignKey(AnimalWool, on_delete=models.DO_NOTHING, related_name='animal_wool')
    nickname = models.CharField(max_length=150, blank=True, verbose_name='nickname')
    is_vaccinated = models.BooleanField(default=False, verbose_name='is_vaccinated')
    is_tail = models.BooleanField(default=False, verbose_name='is_tail')
    date_of_birth = models.DateField(null=True, blank=True, verbose_name='birthday')
    profile_of_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)


class AnimalAddress(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name='address')
    city = models.CharField(max_length=50, verbose_name='city')
    street = models.CharField(max_length=50, verbose_name='street')
    number_of_house = models.CharField(max_length=10, verbose_name='number_of_house')

