# Generated by Django 3.1.7 on 2021-08-17 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='subtitle',
            field=models.CharField(max_length=100, null=True, verbose_name='subtitle :'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(max_length=500, null=True, verbose_name='Description :'),
        ),
    ]
