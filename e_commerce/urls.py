
from django.contrib import admin
from django.urls import path,include
from core.views import frontpage,about

urlpatterns = [
    path('about_page/',about,name="about"),
    path('',include('store.urls')),
    path('',frontpage,name="frontpage"),
    path('admin/', admin.site.urls),

    
]
