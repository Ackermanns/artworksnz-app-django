# Generated by Django 4.0.4 on 2022-05-28 00:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('location', models.CharField(max_length=40)),
                ('primary_media', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Artwork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artwork', models.CharField(max_length=40)),
                ('media_type', models.CharField(max_length=40)),
                ('completion_date', models.DateField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('note', models.TextField()),
                ('artist_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artworksnzapp.artist')),
            ],
        ),
    ]