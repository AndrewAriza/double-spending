from django.urls import path
from . import views

urlpatterns = [
    path('api/blockchain/', views.BlockchainList.as_view()),
    path('api/blockchain/create', views.BlockchainCreate.as_view()),
    path('api/blockchain/reset', views.BlockchainReset.as_view({'get': 'reset'}))
]