# Generated by Django 4.0.4 on 2022-05-25 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('add', '0008_alter_labinfo_buildingnumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='labinfo',
            name='buildingNumber',
            field=models.IntegerField(default=0),
        ),
    ]
