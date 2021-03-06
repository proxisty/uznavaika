# Generated by Django 4.0.1 on 2022-01-17 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedBackHome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Название модели')),
                ('email', models.CharField(blank=True, max_length=120, null=True, verbose_name='Email')),
                ('phone', models.CharField(max_length=15, verbose_name='Телефон')),
                ('description', models.CharField(blank=True, max_length=120, null=True, verbose_name='Описание')),
                ('call_time', models.CharField(blank=True, max_length=120, null=True, verbose_name='Время для звонка')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания обращения')),
            ],
            options={
                'verbose_name': 'Форма обратной связи',
                'verbose_name_plural': 'Формы обратной связи',
            },
        ),
    ]
