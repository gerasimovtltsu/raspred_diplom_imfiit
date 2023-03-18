# Generated by Django 4.1.7 on 2023-03-16 19:02

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0019_alter_record_supervisor_name_alter_topic_supervisor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='topic_title',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='topic_title', chained_model_field='title', on_delete=django.db.models.deletion.CASCADE, to='appointment.topic'),
        ),
    ]