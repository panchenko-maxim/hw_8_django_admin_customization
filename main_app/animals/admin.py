from django.utils.timezone import now

from django.contrib import admin
from django import forms

from .models import AnimalSpecies, AnimalWool, Animal, AnimalAddress

class AnimalAdminForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = '__all__'

    def clean_nickname(self):
        nickname = self.cleaned_data['nickname']
        if len(nickname) < 3:
            raise forms.ValidationError('Nickname must be at least 3 characters long')
        return nickname

    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data['date_of_birth']
        if date_of_birth > now().date():
            raise forms.ValidationError('Date of birth must be before today')
        return date_of_birth


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
    form = AnimalAdminForm
    list_display = ['nickname', 'animal_species', 'is_vaccinated',
                    'owner__nickname', 'date_registration', 'year_birth']
    list_filter = ['is_vaccinated', 'is_tail']
    search_fields = ['nickname', 'owner__nickname']
    ordering = ['nickname']
    list_editable = ['is_vaccinated']
    list_per_page = 2
    readonly_fields = ['date_registration']

    fieldsets = (
        ('Main info', {'fields': ('nickname', 'animal_species', 'animal_wool', 'is_vaccinated', 'is_tail')}),
        ('Dates', {'fields': ('date_of_birth', 'date_registration',)}),
        ('Owner', {'fields': ('owner',)}),

    )

    def year_birth(self, obj):
        return str(obj.date_of_birth.year)
    year_birth.admin_order_field = 'Year birth'





