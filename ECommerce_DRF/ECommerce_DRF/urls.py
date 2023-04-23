
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("products/", include('Product.urls')), # Product
    path("categories/", include('Category.urls')), # Product
    path("users/", include('User.urls')), # Product
    path("carts/", include('Cart.urls')), # Product
    path("payments/", include('Payment.urls')), # Product
    path('token/obtain/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
