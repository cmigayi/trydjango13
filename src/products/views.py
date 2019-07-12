from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm, RawProductForm

# Create your views here.
def product_list(request, *args, **kwargs):
	prods = Product.objects.all() 
	context = {
		"products": prods
	}
	return render(request, 'products/list.html', context)

def product_detail(request, id):	
	prod = get_object_or_404(Product, id=id)
	context = {
		"product": prod
	}
	return render(request, 'products/detail.html', context)

def product_edit(request, id):
	prod = get_object_or_404(Product, id=id)
	form = ProductForm(request.POST or None, instance=prod)
	if form.is_valid():
		form.save()
		redirect("../../")
	context = {
		"form": form
	}
	return render(request, 'products/edit.html', context)

def product_create(request, *args, **kwargs):
	form = ProductForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = ProductForm()
	context = {
		"form": form
	}
	return render(request, 'products/create.html', context)	

def raw_product_form(request, *args, **kwargs):
	form = RawProductForm()
	if request.method == "POST":
		form = RawProductForm(request.POST or None)
		if form.is_valid():
			Product.objects.create(**form.cleaned_data)
		else:
			print(form.errors())	
		form = RawProductForm()
	context = {
		"form": form
	}
	return render(request, 'products/create.html', context)	

def product_delete(request, id):
	prod = Product.objects.get(id=id)
	if request.method == "POST":
		prod.delete() 					
		return redirect("../../")
	context = {
		"product": prod
	}
	return render(request, 'products/delete.html', context)	