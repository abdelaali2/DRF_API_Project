from django.urls import path
from .views import *

urlpatterns = [
    path("categories/", CategoryList.as_view()),
]
