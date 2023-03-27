# Generated by Django 4.1.7 on 2023-03-18 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0023_alter_record_supervisor_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='supervisor_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointment.supervisor', verbose_name='ФИО руководителя'),
        ),
        migrations.AlterField(
            model_name='record',
            name='topic_title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointment.topic', verbose_name='Тема'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='supervisor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointment.supervisor', verbose_name='ФИО руководителя'),
        ),
    ]