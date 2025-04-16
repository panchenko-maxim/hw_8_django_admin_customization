from rest_framework import serializers
from animals.models import Animal


class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = [
            'id', 'owner', 'animal_species', 'animal_wool',
            'nickname', 'date_registration', 'is_vaccinated',
            'is_tail', 'date_of_birth'
        ]
        read_only_fields = ['date_registration']

        def validate_nickname(self, value):
            if value.split() > 1:
                raise serializers.ValidationError('The nickname must consist of one word')
