from rest_framework.viewsets import ModelViewSet

from funfacts.models import FunFact
from funfacts.serializers import FunFactSerializer


class FunFactViewSet(ModelViewSet):
    queryset = FunFact.objects.all()
    serializer_class = FunFactSerializer
