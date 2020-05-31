from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('product/', views.product, name='product'),
    path('customer/', views.customer, name='customer'),
    path('order/', views.order, name='order'),
    path('ship/', views.ship, name='ship'),
    path('vendor/', views.vendor, name='vendor'),

]