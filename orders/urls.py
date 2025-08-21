from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.OrderCreateView.as_view(), name='order-create'),
    path('<int:pk>/', views.OrderDetailView.as_view(), name='order-detail'),
    path('credit-application/', views.CreditApplicationCreateView.as_view(), name='credit-application'),
    path('contact/', views.ContactMessageCreateView.as_view(), name='contact-message'),
]
