# Generated by Django 4.1.7 on 2023-03-16 19:14

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0022_alter_record_supervisor_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='supervisor_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointment.supervisor'),
        ),
        migrations.AlterField(
            model_name='record',
            name='topic_title',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='supervisor_name', chained_model_field='supervisor', on_delete=django.db.models.deletion.CASCADE, to='appointment.topic'),
        ),
    ]
