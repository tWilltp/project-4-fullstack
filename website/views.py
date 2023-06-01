from django.shortcuts import render
from django.views import generic
from .models import Reviews


def home_view(request):
    return render(request, 'index.html')


class ReviewsList(generic.ListView):
    model = Reviews
    queryset = Reviews.objects.filter(status=1).order_by('created_on')
    template_name = 'reviews.html'
    paginate_by = 6
