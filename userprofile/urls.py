from django.urls import path
from django.contrib.auth import views as auth_views
from.import views

urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('login/',auth_views.LoginView.as_view(template_name='userprofile/login.html'),name='login'),
    path('myaccount/',views.myaccount,name='myaccount'),
    path('vendor/<int:pk>/',views.vendor_details,name='vendor_detail')

]