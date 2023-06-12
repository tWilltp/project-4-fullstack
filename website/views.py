from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Reviews, Products
from .forms import CommentForm


def home_view(request):
    return render(request, 'index.html')


class ReviewsList(generic.ListView):
    model = Reviews
    queryset = Reviews.objects.filter(status=1).order_by('created_on')
    template_name = 'reviews.html'
    paginate_by = 6


class ReviewsDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Reviews.objects.filter(status=1)
        reviews = get_object_or_404(queryset, slug=slug)
        comments = reviews.comments.filter(approved=True).order_by(
            'created_on')
        liked = False
        if reviews.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "review_detail.html",
            {
                "reviews": reviews,
                "comments": comments,
                "liked": liked,
                "comment_form": CommentForm(),
            },
        )


class ProductsList(generic.ListView):
    model = Products
    queryset = Products.objects.filter(status=1).order_by('created_on')  # change this to whatever layout you want
    template_name = 'products.html'
    paginate_by = 30


# class BasketList(generic.ListView):
#     model = Basket
#     queryset = Basket.objects.filter(status=1).order_by('created_on')
#     template_name = 'basket.html'
#     paginate_by = 6


def basket_view(request):
    return render(request, 'basket.html')
