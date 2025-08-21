from django.urls import path
from . import views

urlpatterns = [
    path('wishlist/', views.WishlistListView.as_view(), name='wishlist-list'),
    path('wishlist/add/', views.WishlistCreateView.as_view(), name='wishlist-add'),
    path('wishlist/remove/<int:product_id>/', views.remove_from_wishlist, name='wishlist-remove'),
]
