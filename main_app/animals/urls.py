from django.urls import path

from animals.views import AnimalsList, DetailAnimalView, DeleteAnimalView

urlpatterns = [
    path('', AnimalsList.as_view(), name='animals_list'),
    path('animal/<int:pk>', DetailAnimalView.as_view(), name='animals_detail'),
    path('<int:pk>/delete/', DeleteAnimalView.as_view(), name='animal_delete')
]