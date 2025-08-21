from rest_framework import generics, status
from rest_framework.response import Response
from .models import Order, CreditApplication, ContactMessage
from .serializers import OrderSerializer, CreditApplicationSerializer, ContactMessageSerializer

class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderDetailView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class CreditApplicationCreateView(generics.CreateAPIView):
    queryset = CreditApplication.objects.all()
    serializer_class = CreditApplicationSerializer

class ContactMessageCreateView(generics.CreateAPIView):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(
            {'message': 'Xabaringiz muvaffaqiyatli yuborildi!'}, 
            status=status.HTTP_201_CREATED
        )
