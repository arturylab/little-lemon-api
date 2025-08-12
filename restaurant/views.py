from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

from rest_framework import generics
from .models import Menu
from .models import Booking
from .serializers import BookingSerializer
from .serializers import MenuSerializer
from rest_framework import viewsets

# Lista y creación de menús (GET y POST)
class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

# Operaciones sobre un solo menú (GET, PUT, DELETE)
class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingItemsView(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
