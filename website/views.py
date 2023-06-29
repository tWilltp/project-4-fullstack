from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Reviews, Product
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
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm(),
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Reviews.objects.filter(status=1)
        reviews = get_object_or_404(queryset, slug=slug)
        comments = reviews.comments.filter(approved=True).order_by(
            'created_on')
        liked = False
        if reviews.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.comments = reviews
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "review_detail.html",
            {
                "reviews": reviews,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm(),
            },
        )


def all_products(request):
    """ render products """
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'products.html', context)


def products_detail(request):
    """ returns specific product on page"""
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'products_detail.html', context)


# def category(request):
#     category = Category.objects.all()
#     context = {
#         'category': category
#     }
#     return render(request, 'products.html', 'products_detail.html', context)


def basket_view(request):
    return render(request, 'basket.html')
