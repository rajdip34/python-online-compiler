from .models import Index
from .serializers import indexSerializer
from rest_framework import viewsets

class IndexView(viewsets.ModelViewSet):
    queryset = Index.objects.all()
    serializer_class = indexSerializer
    