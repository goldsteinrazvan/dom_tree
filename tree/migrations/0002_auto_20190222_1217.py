# Generated by Django 2.1.7 on 2019-02-22 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tree', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='element',
            name='parent',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='element',
            name='lft',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='element',
            name='rgt',
            field=models.IntegerField(default=0),
        ),
    ]