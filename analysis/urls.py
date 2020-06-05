from django.urls import path
from . import views

urlpatterns = [
    path('', views.analysis, name='analysis'),
    path('competitor/', views.competitor, name='competitor'),
    path('financial/', views.financial, name='financial'),
    path('market/', views.market, name='market'),
    path('products/', views.products, name='products'),

]
