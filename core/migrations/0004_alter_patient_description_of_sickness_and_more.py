# Generated by Django 5.1.3 on 2024-11-08 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_rename_category_physician_alter_physician_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='description_of_sickness',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(max_length=1000),
        ),
    ]
