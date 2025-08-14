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
from rest_framework.permissions import IsAuthenticated

# Lista y creación de menús (GET y POST)
class MenuItemsView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

# Operaciones sobre un solo menú (GET, PUT, DELETE)
class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingItemsView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
