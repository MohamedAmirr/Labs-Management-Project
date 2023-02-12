# Generated by Django 4.0.4 on 2022-05-24 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('add', '0002_remove_lab_floornum'),
    ]

    operations = [
        migrations.AddField(
            model_name='lab',
            name='buildingNum',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='lab',
            name='capacity',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='lab',
            name='floorNum',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='lab',
            name='labId',
            field=models.CharField(default=None, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lab',
            name='numOfChairs',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='lab',
            name='numOfPcs',
            field=models.IntegerField(default=0),
        ),
    ]
