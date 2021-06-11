from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE, SET_NULL
from django.db.models.fields import CharField
from django.db.models.query_utils import select_related_descend

class TypeExpense(models.Model):
    name = CharField(max_length=30, null=False, blank=False, verbose_name='Nombre')

    def __str__(self):
        return self.name

class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE, null=False, blank=False)
    title = models.CharField(max_length=30, null=False, blank=False, verbose_name='Titulo')
    description = models.CharField(max_length=200, null=True, blank=True, default='Sin descripcion', verbose_name='Descripcion')
    amount = models.IntegerField(blank=False, null=False, verbose_name='Monto')
    date = models.DateTimeField(blank=False, null=False, auto_now_add=True)
    typeExpense = models.ForeignKey(TypeExpense, on_delete=SET_NULL, null=True)

    def __str__(self):
        return f'{self.user}:{self.pk}-{self.typeExpense}'

