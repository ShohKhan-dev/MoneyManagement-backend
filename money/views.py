
# Rest-Framework
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAdminUser
from django_filters import rest_framework as filters

# Project
from money.serializers import TagSerializer, TransactionSerializer
from money.models import Tag, Transaction


class TagViewSet(ModelViewSet):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()


class TransactionViewSet(ModelViewSet):
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('tag',)



__all__ = ['TagViewSet', 'TransactionViewSet']
