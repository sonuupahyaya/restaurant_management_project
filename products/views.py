# products/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class MenuListView(APIView):
    def get(self, request):
            """
            Returns a list of menu items.
            Currently uses a hardcoded list, but later this
            will be replaced with a database query.
            """
            menu_items = [
                {
                    "id": 1,
                    "name": "Margherita Pizza",
                    "price": 8.99,
                    "category": "Pizza"
                },
                {
                   "id": 2,
                   "name": "Pepperoni Pizza",
                   "price": 10.99,
                   "category": "Pizza"
                },
                {
                   "id": 3,
                   "name": "Caesar Salad",
                   "price": 6.50,
                   "category": "Salad"
                },
                {
                   "id": 4,
                   "name": "Spaghetti Bolognese",
                   "price": 12.00,
                   "category": "Pasta"
                }
            ]
 return Response(menu_items, status=status.HTTP_200_OK)
