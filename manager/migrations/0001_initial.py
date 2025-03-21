# Generated by Django 5.1.6 on 2025-03-20 07:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Sarlavhasi')),
                ('description', models.TextField(default="Ma'lumot qo'shilmadi.", verbose_name='Tavsifi')),
                ('url', models.CharField(max_length=50, unique=True, verbose_name='Havolasi')),
                ('image', models.ImageField(upload_to='images/', verbose_name='Surati')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name="Qo'shilgan vaqti")),
            ],
            options={
                'verbose_name': 'Loyiha ',
                'verbose_name_plural': 'Loyihalar',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Texnalogiya')),
            ],
            options={
                'verbose_name': 'Texnalogiya ',
                'verbose_name_plural': 'Texnalogiyalar',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('portfolio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='manager.portfolio')),
            ],
        ),
        migrations.AddField(
            model_name='portfolio',
            name='technologies',
            field=models.ManyToManyField(related_name='technologies', to='manager.technology', verbose_name='Texnalogiyalari'),
        ),
    ]
