from django.urls import path
from . import views

app_name = 'fraud_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('transactions/', views.transactions_list, name='transactions'),
    path('alerts/', views.alerts, name='alerts'),
    path('upload/', views.upload_csv, name='upload_csv'),
    path('login/', views.user_login, name='login'),
]