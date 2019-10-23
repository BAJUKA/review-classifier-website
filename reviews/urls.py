from django.urls import include, path
from . import views

app_name='chat'

urlpatterns = [
    path('kerala_floods/', views.Kerala_FloodsView, name='kerala_floods'),
    path('cyclone_titli/', views.Cyclone_TitliView, name='cyclone_titli'),
    path('indonesian_tsunami/', views.Indonesian_TsunamiView, name='indonesian_tsunami'),
    path('hurricane_michael/', views.Hurricane_MichaelView, name='hurricane_michael'),
]