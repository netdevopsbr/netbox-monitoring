from django.urls import path
from . import models, views

urlpatterns = (
    path('', views.HomeView.as_view(), name='home'),
)