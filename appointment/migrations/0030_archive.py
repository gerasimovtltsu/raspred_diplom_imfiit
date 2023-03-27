# Generated by Django 4.1.7 on 2023-03-27 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0029_delete_archive'),
    ]

    operations = [
        migrations.CreateModel(
            name='Archive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='ФИО студента')),
                ('supervis_name', models.CharField(max_length=255, verbose_name='ФИО руководителя')),
                ('top_title', models.CharField(max_length=255, verbose_name='Название темы')),
                ('date_post', models.DateTimeField(auto_now_add=True, verbose_name='Дата записи')),
            ],
        ),
    ]