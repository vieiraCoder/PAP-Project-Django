# Generated by Django 3.1.3 on 2020-12-15 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0004_auto_20201213_2133'),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='liked',
            field=models.ManyToManyField(blank=True, related_name='likes', to='perfil.Profile'),
        ),
    ]
