from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django_filters.rest_framework import DjangoFilterBackend

from animals_restfull.authentication import CustomJWTAuthentication
from animals_restfull.utils import generate_jwt_token, creat_token_for_user

from animals.models import Animal
from animals_restfull.serializers import AnimalSerializer


class AnimalModelViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    # filterset_fields = ['owner', 'animal_species', 'is_vaccinated', 'is_tail']
    search_fields = ['nickname', 'animal_species']
    ordering_fields = ['date_registration']
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

@api_view(["POST"])
@permission_classes([])
def login(request):
    nickname = request.data.get("nickname")
    password = request.data.get("password")

    user = authenticate(username=nickname, password=password)
    if user:
        token = creat_token_for_user(user)
        return Response({
            "token": token.key,
            "expires_at": token.expires_at,
            "role": "staff" if any([user.is_staff, user.is_superuser]) else "member"
        })
    return Response({"error": "Wrong credentials"}, status=401)

@api_view(["POST"])
@permission_classes([])
def login_jwt(request):
    nickname = request.data.get("nickname")
    password = request.data.get("password")

    user = authenticate(username=nickname, password=password)
    if user:
        token = generate_jwt_token(user)
        return Response({
            "access_key": token
        })
    return Response({"error": "Wrong credentials"}, status=401)