# Generated by Django 3.1 on 2020-12-13 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0003_relationship'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='background',
            field=models.ImageField(default='bckg.jpg', upload_to=''),
        ),
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(max_length=200),
        ),
    ]
