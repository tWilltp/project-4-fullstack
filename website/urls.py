from . import views
from django.urls import include, path

urlpatterns = [
    path('', views.home_view, name='home'),
    path('templates/', views.ReviewsList.as_view(), name='reviews'),
    path('templates/products.html', views.all_products, name='products'),
    path('templates/products_detail.html', views.products_detail, name='products_detail'),
    path('templates/basket.html', views.basket_view, name='basket'),
    path('reviews/<slug:slug>/', views.ReviewsDetail.as_view(
        ), name='review_detail'),
]
