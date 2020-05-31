from django.urls import path
from . import views

urlpatterns = [
    path('', views.finance, name='finance'),
    path('revenue/', views.revenue, name='revenue'),
    path('sales/', views.sales, name='sales'),
    path('expense/', views.expense, name='expense'),
]