# Generated by Django 3.0.2 on 2020-01-20 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TV',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('genre', models.CharField(blank=True, max_length=10, null=True)),
                ('photo', models.ImageField(blank=True, max_length=1000, null=True, upload_to='movie_photos')),
                ('cast', models.CharField(max_length=9999)),
                ('plot', models.CharField(max_length=9999)),
                ('synopsis', models.CharField(max_length=999999)),
                ('dir', models.CharField(blank=True, help_text='Put the link to your TV series directory', max_length=1000, null=True)),
                ('imdb_found', models.BooleanField(blank=True, default=False, null=True)),
                ('manual', models.BooleanField(default=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]