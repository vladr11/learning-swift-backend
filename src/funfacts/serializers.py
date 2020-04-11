from rest_framework import serializers

from funfacts.models import FunFact


class FunFactSerializer(serializers.ModelSerializer):
    class Meta:
        model = FunFact
        fields = ("id", "title", "description", "created_at", "modified_at")
