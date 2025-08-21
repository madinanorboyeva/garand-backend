from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Wishlist
from .serializers import WishlistSerializer

class WishlistListView(generics.ListAPIView):
    serializer_class = WishlistSerializer
    
    def get_queryset(self):
        # Bu yerda authentication qo'shilganda user.id ishlatiladi
        # Hozircha barcha wishlistlarni qaytaramiz
        return Wishlist.objects.all()

class WishlistCreateView(generics.CreateAPIView):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer

@api_view(['DELETE'])
def remove_from_wishlist(request, product_id):
    try:
        # Bu yerda authentication qo'shilganda request.user ishlatiladi
        # Hozircha product_id bo'yicha o'chiramiz
        wishlist_item = Wishlist.objects.get(product_id=product_id)
        wishlist_item.delete()
        return Response({'message': 'Sevimlilardan o\'chirildi'}, status=status.HTTP_200_OK)
    except Wishlist.DoesNotExist:
        return Response({'error': 'Mahsulot topilmadi'}, status=status.HTTP_404_NOT_FOUND)

