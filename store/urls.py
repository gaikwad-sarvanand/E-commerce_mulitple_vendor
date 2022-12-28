from django.urls import path
from .import views

urlpatterns = [
    path('search/',views.search,name="search"),
    path('cart/',views.cart_view,name='cart_view'),
    path('change-quantity/<str:product_id>',views.change_quantity,name='change_quantity'),
    path('remove-from-cart/<str:product_id>/',views.remove_from_cart,name='remove_from_cart'),
    path('<slug:slug>/',views.category_detail,name='category_detail'),
    path('cart/checkout/',views.checkout,name='checkout'),
    path('cart/success/',views.success,name='success'),
    path('add-to-cart/<int:product_id>/',views.add_to_cart,name='add_to_cart'),
    path('<slug:category_slug>/<slug:slug>/',views.product_details,name='product_details'),
]
