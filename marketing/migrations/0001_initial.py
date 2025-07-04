# Generated by Django 3.2.25 on 2025-06-30 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContestEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('nombre', models.CharField(max_length=100)),
                ('anime_fav', models.CharField(max_length=100)),
                ('creado', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
