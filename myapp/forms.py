from django.contrib.auth import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import RequestAborted, ValidationError
from django.forms.models import modelform_factory
from . import models
from .models import Expense, TypeExpense

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        try:
            user = models.User.objects.get(email = self.cleaned_data('email'))
            if user != None:
                raise ValidationError('Email ocupado')
            return self.cleaned_data.get('email')
        except models.User.DoesNotExist:
            return self.cleaned_data.get('email')
        
class createExpenseForm(ModelForm):
    class Meta:
        model = Expense
        fields = ['title', 'typeExpense', 'description', 'amount']

class EditExpenseForm(ModelForm):
    class Meta:
        model = Expense
        fields = ['title', 'typeExpense', 'description', 'amount']
