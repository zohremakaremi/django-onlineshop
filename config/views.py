from django.shortcuts import render
from django.views import View
from eshop_menu.models import Menu


class Header(View):
	def get(self, request):
		menus = Menu.objects.filter(is_sub=False)
		
			
		return render(request, 'shared/Header.html', { 'menus':menus})

# footer code behind
def footer(request, *args, **kwargs):
   

    return render(request, 'shared/Footer.html',{})