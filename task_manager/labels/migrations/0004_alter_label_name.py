# Generated by Django 5.0.6 on 2024-06-11 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labels', '0003_alter_label_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='label',
            name='name',
            field=models.CharField(max_length=255, unique=True, verbose_name='Label name'),
        ),
    ]
