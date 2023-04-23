from django.urls import path
from .views import *


urlpatterns = [
    path('payments/', PaymentListAPIView.as_view(), name='payment-list'),
    path('shipments/', ShipmentListCreateAPIView.as_view(), name='shipment-list'),
    path('shipments/<int:pk>/', ShipmentRetrieveUpdateDestroyAPIView.as_view(), name='shipment-detail'),
    path('payments/create/', PaymentCreateAPIView.as_view(), name='payment-create'),
    path('payments/<int:pk>/', PaymentRetrieveUpdateDestroyAPIView.as_view(), name='payment-detail'),
]