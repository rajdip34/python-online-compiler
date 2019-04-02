from rest_framework import viewsets
from .models import Calendar
from .serializers import CalenderSerializer

class CalendarView(viewsets.ModelViewSet):
    queryset = Calendar.objects.all()
    serializer_class = CalenderSerializer
