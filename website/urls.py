from . import views
from django.urls import include, path

urlpatterns = [
    path('', views.home_view, name='home'),
    path('templates/', views.ReviewsList.as_view(), name='reviews'),
]
