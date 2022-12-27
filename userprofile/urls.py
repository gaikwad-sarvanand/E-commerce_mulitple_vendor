from django.urls import path
from django.contrib.auth import views as auth_views
from.import views

urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('login/',auth_views.LoginView.as_view(template_name='userprofile/login.html'),name='login'),
    path('myaccount/',views.myaccount,name='myaccount'),
    path('my-store/',views.mystore,name='my-store'),
    path('my-store/order-detail/<int:pk>/',views.my_store_order_detail,name="my_store_order_detail"),
    path('my-store/add-product/',views.add_product,name='add_product'),
    path('my-store/edit-product/<int:pk>/',views.edit_product,name='edit_product'),
    path('my-store/delete-product/<int:pk>/',views.delete_product,name='delete_product'),
    path('vendor/<int:pk>/',views.vendor_details,name='vendor_detail')

]
