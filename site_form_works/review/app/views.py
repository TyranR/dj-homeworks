from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse

from .models import Product, Review
from .forms import ReviewForm


def product_list_view(request):
    template = 'app/product_list.html'
    products = Product.objects.all()

    context = {
        'product_list': products,
    }

    return render(request, template, context)


def product_view(request, pk):
    template = 'app/product_detail.html'
    product = get_object_or_404(Product, id=pk)
    form = ReviewForm
    key_exists = 'reviewed_products' in request.session
    if not key_exists:
        request.session['reviewed_products'] = []
        reviewed_products = []
    else:
        reviewed_products = request.session['reviewed_products']
    if request.method == 'GET':
        if not pk in reviewed_products:
            is_review_exist = 0
        else:
            is_review_exist = 1
    if request.method == 'POST':
        if not pk in reviewed_products:
            text = request.POST.get('text')
            new_review = Review.objects.create(text=text, product=product)
            reviewed_products.append(pk)
            request.session['reviewed_products'] = reviewed_products
            is_review_exist = 0
        else:
            is_review_exist = 1
    all_review = Review.objects.filter(product__id=pk)
    print(request.session['reviewed_products'])
    context = {
        'form': form,
        'product': product,
        'reviews': all_review,
        'is_review_exist': is_review_exist
    }

    return render(request, template, context)
