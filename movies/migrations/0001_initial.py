# Generated by Django 2.2.3 on 2019-07-17 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('year', models.IntegerField()),
                ('type', models.CharField(choices=[('action', 'Action'), ('horror', 'Horror'), ('adventure', 'Adventure'), ('scifi', 'Science Fiction'), ('romance', 'Romance'), ('drama', 'Drama'), ('thriller', 'Thriller')], max_length=8)),
                ('industry', models.CharField(choices=[('HW', 'Hollywood'), ('BW', 'Bollywood'), ('TM', 'Tamil'), ('OT', 'Others')], max_length=3)),
                ('photo', models.ImageField(max_length=1000, upload_to='photos')),
                ('video', models.CharField(help_text='Put the link to your movie file', max_length=1000)),
            ],
        ),
    ]