from django.urls import path, include

from . import views

urlpatterns = [
path('', views.HomeView.as_view(), name="home"),
path('pos', views.PosView.as_view(), name="positive"),
path('neg', views.NegView.as_view(), name="negative"),
]
