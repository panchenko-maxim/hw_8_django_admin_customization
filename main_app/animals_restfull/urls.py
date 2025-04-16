from django.urls import path, include
from rest_framework.routers import DefaultRouter
from animals_restfull.views import AnimalModelViewSet, login_jwt


router = DefaultRouter()
router.register(r'animals', AnimalModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('login/', login, name="login"),
    path('login-jwt/', login_jwt, name='login-jwt'),
]