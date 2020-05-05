from django.shortcuts import render
from phones.models import Phone


def show_catalog(request):
    template = 'catalog.html'
    all_entries = Phone.objects.all()
    sort = request.GET.get('sort')
    if sort == 'name':
        all_entries = Phone.objects.all().order_by('title')
    elif sort == 'min-price':
        all_entries = Phone.objects.all().order_by('price')
    elif sort == 'max-price':
        all_entries = Phone.objects.all().order_by('-price')
    else:
        all_entries = Phone.objects.all()
    context = {'phones': all_entries}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    all_entries = Phone.objects.filter(slug='samsung-galaxy-edge-2')
    context = {'telephone': all_entries}
    print(context)
    return render(request, template, context)


def base_view(request):
    template = 'base.html'
    context = {}
    return render(request, template, context)
