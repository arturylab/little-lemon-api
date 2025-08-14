# pruebas/test_views.py
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from django.contrib.auth.models import User


class MenuViewTest(TestCase):
    def setUp(self):
        # Crear usuario y autenticación
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client = APIClient()
        self.client.login(username='testuser', password='testpass')

        # Crear datos de prueba
        self.menu1 = Menu.objects.create(Title="Pizza", Price=12.00, Inventory=20)
        self.menu2 = Menu.objects.create(Title="Pasta", Price=10.00, Inventory=15)

    def test_getall(self):
        url = reverse('menu-list')
        response = self.client.get(url)

        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
