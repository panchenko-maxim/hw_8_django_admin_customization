from django.forms.models import model_to_dict
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView

from animals.mixins import (LoggingMixin, OwnerRequiredMixin,
                            AnimalVisibilityMixin, AddContextExtraInfoMixin,
                            StopDogDeleteMixin, SortingMixin, CountObjectsMixin)
from animals.models import Animal


class AnimalsList(LoggingMixin, SortingMixin, CountObjectsMixin, AnimalVisibilityMixin, ListView):
    model = Animal
    context_object_name = 'animals'
    template_name = 'animals/animals_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["animals"] = [model_to_dict(animal) for animal in self.object_list]
        return context

class DetailAnimalView(OwnerRequiredMixin, LoggingMixin, AddContextExtraInfoMixin, DetailView):
    model = Animal
    context_object_name = 'animal'
    template_name = "animals/detail_animal.html"

class DeleteAnimalView(LoggingMixin, StopDogDeleteMixin, DeleteView):
    model = Animal
    template_name = 'animals/confirm_delete.html'
    success_url = reverse_lazy('animals_list')
    success_message = "Animal is deleted."

