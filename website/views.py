from django.shortcuts import render
from django.views import generic
from .models import Reviews, Products


def home_view(request):
    return render(request, 'index.html')


class ReviewsList(generic.ListView):
    model = Reviews
    queryset = Reviews.objects.filter(status=1).order_by('created_on')
    template_name = 'reviews.html'
    paginate_by = 6


class ProductsList(generic.ListView):
    model = Products
    queryset = Products.objects.filter(status=1).order_by('created_on') # change this to whatever layout you want
    template_name = 'products.html'
    paginate_by = 30
