# Generated by Django 2.1.2 on 2018-10-28 07:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=255)),
                ('subcategory', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Favourites',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Location_Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('latitude', models.CharField(max_length=255)),
                ('longitude', models.CharField(max_length=255)),
                ('place', models.CharField(max_length=255)),
                ('contact_name', models.CharField(max_length=255)),
                ('contact_num', models.CharField(max_length=255)),
                ('contact_email', models.CharField(max_length=255)),
                ('website', models.CharField(max_length=255)),
                ('cost', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=4095)),
                ('date', models.DateField()),
                ('user', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Saved_Searches',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=255)),
                ('search', models.CharField(max_length=255)),
                ('user', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Suggestions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suggestion', models.CharField(max_length=6000)),
                ('loc', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='codeforgood.Locations')),
                ('user', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=255)),
                ('accessibility', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Warnings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('warning', models.CharField(max_length=255)),
                ('loc', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='codeforgood.Locations')),
            ],
        ),
        migrations.AddField(
            model_name='location_tags',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='codeforgood.Locations'),
        ),
        migrations.AddField(
            model_name='location_tags',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='codeforgood.Tags'),
        ),
        migrations.AddField(
            model_name='favourites',
            name='favourite_loc',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='codeforgood.Locations'),
        ),
        migrations.AddField(
            model_name='favourites',
            name='user',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]