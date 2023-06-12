from . import views
from django.urls import include, path

urlpatterns = [
    path('', views.home_view, name='home'),
    path('templates/', views.ReviewsList.as_view(), name='reviews'),
    path('templates/products.html', views.ProductsList.as_view(), name='products'),
    # path('templates/basket.html', views.BasketList.as_view(), name='basket_item'),
    path('templates/basket.html', views.basket_view, name='basket'),
    path('reviews/<slug:slug>/', views.ReviewsDetail.as_view(
        ), name='review_detail'),
]
