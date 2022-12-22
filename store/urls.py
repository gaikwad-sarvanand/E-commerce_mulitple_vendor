from django.urls import path
from .import views

urlpatterns = [
    path('search/',views.search,name="search"),
    path('<slug:slug>/',views.category_detail,name='category_detail'),
    path('add-to-cart/<int:product_id>/',views.add_to_cart,name='add_to_cart'),
    path('<slug:category_slug>/<slug:slug>/',views.product_details,name='product_details'),
]
