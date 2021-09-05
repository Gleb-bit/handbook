from django_filters import rest_framework
from rest_framework import viewsets

from .models import Handbook, Element
from .serializers import HandbookSerializer, ElementSerializer


class HandbookFilter(rest_framework.FilterSet):
    '''Filter for handbook'''

    class Meta:
        model = Handbook
        fields = ['title', 'start_date', 'version']


class HandbookViewSet(viewsets.ModelViewSet):
    '''Information about handbook'''

    queryset = Handbook.objects.all()
    serializer_class = HandbookSerializer
    filter_backends = (rest_framework.DjangoFilterBackend,)
    filterset_class = HandbookFilter


class ElementViewSet(viewsets.ModelViewSet):
    '''Information about element of handbook'''

    queryset = Element.objects.all()
    serializer_class = ElementSerializer
