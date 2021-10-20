from django.urls import path
from customers.views import create_customer, read_customer, update_customer, delete_customer, list_customers

app_name = 'customers'

urlpatterns = [
    path('create/', create_customer, name='create'),
    path('<int:pk>/read/', read_customer, name='read'),
    path('<int:pk>/update/', update_customer, name='update'),
    path('<int:pk>/delete/', delete_customer, name='delete'),
    path('list/', list_customers, name='list'),
]