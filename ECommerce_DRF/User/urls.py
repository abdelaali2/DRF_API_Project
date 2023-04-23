from django.urls import path
from .views import *

urlpatterns = [
    path("users/<int:pk>", UserList.as_view()),
]
