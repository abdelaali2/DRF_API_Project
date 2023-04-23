from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Shipment, Payment, Cart
from .serializers import ShipmentSerializer, PaymentSerializer
from Cart.serializers import CartSerializer


class PaymentListAPIView(generics.ListAPIView):
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Payment.objects.filter(user=self.request.user)


class PaymentCreateAPIView(generics.CreateAPIView):
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]


class PaymentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Payment.objects.filter(user=self.request.user)


class ShipmentListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ShipmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Shipment.objects.filter(user=self.request.user).select_related("cart")

    def perform_create(self, serializer):
        cart = Cart.objects.get_or_create(user=self.request.user)[0]
        serializer.save(user=self.request.user, cart=cart)


class ShipmentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ShipmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Shipment.objects.filter(user=self.request.user).select_related("cart")

    def perform_update(self, serializer):
        cart = Cart.objects.get_or_create(user=self.request.user)[0]
        serializer.save(user=self.request.user, cart=cart)
