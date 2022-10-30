from django.shortcuts import render, redirect
from django.views import View
from .forms import UserRegistrationForm, VerifyCodeForm, UserLoginForm
import random
from utils import send_otp_code
from .models import OtpCode, User
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin


class UserRegisterView(View):
	form_class = UserRegistrationForm
	template_name = 'accounts/register.html'

	def get(self, request):
		register_form = self.form_class
		return render(request, self.template_name, {'register_form':register_form})

	def post(self, request):
		register_form = self.form_class(request.POST)
		if register_form.is_valid():
			random_code = random.randint(1000, 9999)
			send_otp_code(register_form.cleaned_data['phone'], random_code)
			OtpCode.objects.create(phone_number=register_form.cleaned_data['phone'], code=random_code)
			request.session['user_registration_info'] = {
				'phone_number': register_form.cleaned_data['phone'],
				'email': register_form.cleaned_data['email'],
				'full_name': register_form.cleaned_data['full_name'],
				'password': register_form.cleaned_data['password'],
			}
			messages.success(request, 'we sent you a code', 'success')
			return redirect('eshop_accounts:verify_code')
		return render(request, self.template_name, {'register_form':register_form})


class UserRegisterVerifyCodeView(View):
	form_class = VerifyCodeForm

	def get(self, request):
		form = self.form_class
		return render(request, 'accounts/verify.html', {'form':form})

	def post(self, request):
		user_session = request.session['user_registration_info']
		code_instance = OtpCode.objects.get(phone_number=user_session['phone_number'])
		form = self.form_class(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			if cd['code'] == code_instance.code:
				User.objects.create_user(user_session['phone_number'], user_session['email'],
										 user_session['full_name'], user_session['password'])

				code_instance.delete()
				messages.success(request, 'you registered.', 'success')
				return redirect('eshop_products:product_list')
			else:
				messages.error(request, 'this code is wrong', 'danger')
				return redirect('eshop_accounts:verify_code')
		return redirect('eshop_products:product_list')


class UserLogoutView(LoginRequiredMixin, View):
	def get(self, request):
		logout(request)
		messages.success(request, 'you logged out successfully', 'success')
		return redirect('eshop_accounts:user_login')


class UserLoginView(View):
	form_class = UserLoginForm
	template_name = 'accounts/login.html'

	def get(self, request):
		login_form = self.form_class
		return render(request, self.template_name, {'login_form':login_form})

	def post(self, request):
		login_form = self.form_class(request.POST)
		if login_form.is_valid():
			cd = login_form.cleaned_data
			user = authenticate(request, phone_number=cd['phone'], password=cd['password'])
			if user is not None:
				login(request, user)
				messages.success(request, 'you logged in successfully', 'info')
				return redirect('eshop_products:product_list')
			messages.error(request, 'phone or password is wrong', 'warning')
		return render(request, self.template_name, {'login_form':login_form})
