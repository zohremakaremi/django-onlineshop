from django import forms
from django.core import validators
    


class CreateContactForm(forms.Form):
        full_name = forms.CharField(
            widget=forms.TextInput(
                attrs={'class': 'form-control'}),
            label='نام و نام خانوادگی',
            validators=[
                validators.MaxLengthValidator(150, 'نام و نام خانوادگی شما نمیتواند بیشتر از 150 کاراکتر باشد')
            ]
        )

        email = forms.EmailField(
            widget=forms.EmailInput(attrs={'class': 'form-control'}),
            label='ایمیل',
            validators=[
                validators.MaxLengthValidator(100, 'ایمیل شما نمیتواند بیشتر از 100 کاراکتر باشد')
            ]
        )

        subject = forms.CharField(
            widget=forms.TextInput(attrs={ 'class': 'form-control'}),
            label='عنوان',
            validators=[
                validators.MaxLengthValidator(200, 'عنوان پیام شما نمیتواند بیشتر از 200 کاراکتر باشد')
            ]
        )

        text = forms.CharField(
            widget=forms.Textarea(
                attrs={'class': 'form-control', 'rows': '8',
                    'cols': '20'}),
            label='متن پیام'
        )
