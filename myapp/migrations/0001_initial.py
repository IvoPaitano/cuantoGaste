# Generated by Django 3.2.4 on 2021-06-08 17:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TypeExpense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Nombre')),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Titulo')),
                ('description', models.CharField(blank=True, max_length=200, null=True, verbose_name='Descripcion')),
                ('amount', models.IntegerField(verbose_name='Monto')),
                ('typeExpense', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.typeexpense')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
