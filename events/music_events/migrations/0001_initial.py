# Generated by Django 4.1.3 on 2022-12-02 01:25

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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('show_date', models.DateTimeField()),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music_events.artist')),
                ('venue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music_events.venue')),
            ],
        ),
    ]
