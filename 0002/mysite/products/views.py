from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory
from django.shortcuts import render, redirect
from django.views.generic import View

from .forms import CategoryForm, ProductForm
from .models import Category, Product


@login_required
def products_list(request):
    products = Product.objects.filter(user=request.user)
    return render(request, 'products/products_list.html', {'products': products})


@login_required
def new_product(request):
    if request.method == 'POST':
        form = ProductForm(request.user, request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return redirect('products_list')
    else:
        form = ProductForm(request.user)
    return render(request, 'products/product_form.html', {'form': form})


@login_required
def new_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return redirect('products_list')
    else:
        form = CategoryForm()
    return render(request, 'products/category_form.html', {'form': form})


@login_required
def edit_all_products(request):
    ProductFormSet = modelformset_factory(Product, fields=('name', 'price', 'category'), extra=0)
    data = request.POST or None
    formset = ProductFormSet(data=data, queryset=Product.objects.filter(user=request.user))
    for form in formset:
        form.fields['category'].queryset = Category.objects.filter(user=request.user)

    if request.method == 'POST' and formset.is_valid():
        formset.save()
        return redirect('products_list')

    return render(request, 'products/products_formset.html', {'formset': formset})
