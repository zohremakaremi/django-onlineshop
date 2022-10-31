
from django.urls import path
from . import views
app_name = 'eshop_products'

urlpatterns = [
    
	path('list/', views.ListView.as_view(), name='product_list'),
	path('category/<slug:category_slug>/', views.ListView.as_view(), name='category_filter'),
	path('<slug:slug>/', views.ProductDetailView.as_view(), name='product_detail'),
]
   
