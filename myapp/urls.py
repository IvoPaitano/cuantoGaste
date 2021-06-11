from django.urls import path
from .import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('register/', views.registerUser, name='register'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('expenses/', views.expenses, name='expenses'),
    path('expenses/edit/<int:id>', views.editExpense, name='editExpenses'),
    path('expenses/delete/<int:id>', views.deleteExpense, name='deleteExpenses'),
]