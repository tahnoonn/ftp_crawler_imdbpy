# Generated by Django 2.2.3 on 2019-07-19 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='photo',
            field=models.FileField(max_length=1000, upload_to='photos'),
        ),
    ]