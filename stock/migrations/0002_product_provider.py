# Generated by Django 3.0.4 on 2020-03-09 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='provider',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='stock.Provider'),
        ),
    ]
