
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("product/", include('Product.urls')), # Product
    path("category/", include('Category.urls')), # Product
    path("cart/", include('Cart.urls')), # Product
    path("User/", include('user.urls')), # Product
    path("payment/", include('Payment.urls')), # Product
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
