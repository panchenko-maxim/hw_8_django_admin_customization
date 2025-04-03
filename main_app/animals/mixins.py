import logging

from django.core.exceptions import PermissionDenied
from django.utils.timezone import now
from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy

from animals.models import Animal

logger = logging.getLogger('__main__')

class LoggingMixin:
    def dispatch(self, request, *args, **kwargs):
        logger.info(f"[{now()}] {request.method} {request.path} - {request.user.nickname}")
        return super().dispatch(request, *args, **kwargs)


class OwnerRequiredMixin:
    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        if obj.owner != self.request.user:
            raise PermissionDenied("You are not the owner of this animal!")
        return obj

class AnimalVisibilityMixin:
    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Animal.objects.all()
        if user.is_authenticated:
            return Animal.objects.filter(owner=user)

class AddContextExtraInfoMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["extra_info"] = "Some extra info"
        return context

class StopDogDeleteMixin:
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.animal_species != "dog":
            messages.error(request, "You can't delete this animal!")
            return redirect('animals_list')
        return super().dispatch(request, *args, **kwargs)

class SortingMixin:
    default_sort_field = 'nickname'

    def get_queryset(self):
        queryset = super().get_queryset()
        sort_field = self.request.GET.get('sort', self.default_sort_field)
        return queryset.order_by(sort_field)

class CountObjectsMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_count'] = self.get_queryset().count()
        return context

class ObjectExistenceMixin:
    def dispatch(self, request, *args, **kwargs):
        self.object = get_object_or_404(self.model, pk=kwargs['pk'])
        return super().dispatch(request, *args, **kwargs)

class UserHasPermissionMixin:
    required_permission = 'can_change_object'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm(self.required_permission):
            raise PermissionDenied("You don't have permission 'can_change_object'!")
        return super().dispatch(request, *args, **kwargs)

class RedirectAfterActionMixin:
    redirect_url = reverse_lazy('animals_list')
    def get_success_url(self):
        return self.redirect_url

