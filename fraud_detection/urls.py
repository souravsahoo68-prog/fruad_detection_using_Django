from django.contrib import admin
from django.urls import path, include
from fraud_app import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('', include('fraud_app.urls')),
]