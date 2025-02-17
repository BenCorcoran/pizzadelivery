from django import forms
from .models import Pizza, DeliveryDetails
from django.contrib.auth.models import User
import datetime

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', "Passwords do not match")

        return cleaned_data

class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['size', 'crust', 'sauce', 'cheese', 
                  'pepperoni', 'chicken', 'ham', 'pineapple', 
                  'peppers', 'mushrooms', 'onions']
        widgets = {
            'size': forms.Select(attrs={'class': 'form-control'}),
            'crust': forms.Select(attrs={'class': 'form-control'}),
            'sauce': forms.Select(attrs={'class': 'form-control'}),
            'cheese': forms.Select(attrs={'class': 'form-control'}),
            'pepperoni': forms.CheckboxInput(),
            'chicken': forms.CheckboxInput(),
            'ham': forms.CheckboxInput(),
            'pineapple': forms.CheckboxInput(),
            'peppers': forms.CheckboxInput(),
            'mushrooms': forms.CheckboxInput(),
            'onions': forms.CheckboxInput(),
        }

class DeliveryDetailsForm(forms.ModelForm):
    card_number = forms.CharField(
        max_length=16, 
        min_length=16, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '1234567812345678'})
    )
    card_expiry_date = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'MM/YYYY'})
    )
    card_cvv = forms.CharField(
        max_length=3, 
        min_length=3, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '123'})
    )

    class Meta:
        model = DeliveryDetails
        fields = ['name', 'address', 'card_number', 'card_expiry_date', 'card_cvv']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_card_number(self):
        card_number = self.cleaned_data.get('card_number')
        if not card_number.isdigit():
            raise forms.ValidationError("Card number must contain only digits.")
        return card_number

    def clean_card_expiry_date(self):
        expiry_date_str = self.cleaned_data.get('card_expiry_date')
        try:
            month, year = map(int, expiry_date_str.split('/'))
            expiry_date = datetime.date(year, month, 1)
            if expiry_date < datetime.date.today().replace(day=1):
                raise forms.ValidationError("Card expiry date must be in the future.")
        except ValueError:
            raise forms.ValidationError("Invalid date format. Use MM/YYYY.")
        return expiry_date_str

    def clean_card_cvv(self):
        card_cvv = self.cleaned_data.get('card_cvv')
        if not card_cvv.isdigit():
            raise forms.ValidationError("CVV must contain only digits.")
        return card_cvv