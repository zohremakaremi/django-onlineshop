from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Product, Category
from django.contrib import messages
from utils import IsAdminUserMixin
from eshop_slider.models import Slider
from eshop_order.forms import CartAddForm


class ListView(View):
	paginate_by = 10
	def get(self, request, category_slug=None):
		products = Product.objects.filter(available=True)
		categories = Category.objects.filter(is_sub=False)
		if category_slug:
			category = Category.objects.get(slug=category_slug)
			products = products.filter(category=category)
		return render(request, 'eshop_products/list.html', {'products':products, 'categories':categories})
class ProductDetailView(View):
	def get(self, request, slug):
		product = get_object_or_404(Product, slug=slug)
		form = CartAddForm()
		return render(request, 'eshop_products/detail.html', {'product':product, 'form':form})
