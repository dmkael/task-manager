# Generated by Django 5.0.6 on 2024-06-10 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labels', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='label',
            name='name',
            field=models.CharField(max_length=255, unique=True, verbose_name='Name'),
        ),
    ]
