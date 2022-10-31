
from django.urls import path
from . import views
app_name = 'eshop_products'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
	path('products/', views.ListView.as_view(), name='product_list'),
	path('products/category/<slug:category_slug>/', views.ListView.as_view(), name='category_filter'),
	path('products/<slug:slug>/', views.ProductDetailView.as_view(), name='product_detail'),
]
   
