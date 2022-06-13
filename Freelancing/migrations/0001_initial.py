# Generated by Django 4.0.5 on 2022-06-13 06:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=40)),
                ('displayName', models.CharField(max_length=40)),
                ('tagline', models.CharField(max_length=30)),
                ('contactNumber', models.IntegerField()),
                ('language', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to='images/')),
                ('description', models.TextField()),
                ('customer', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SocialLinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.URLField()),
                ('twitter', models.URLField()),
                ('linkedlin', models.URLField()),
                ('behance', models.URLField()),
                ('dribble', models.URLField()),
                ('customer', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Freelancing.customer')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('price', models.ImageField(upload_to='')),
                ('priceType', models.CharField(choices=[('HOURLY RATE', 'HOURLY RATE'), ('HALF DAY RATE', 'HALF DAY RATE'), ('FULL DAY RATE', 'FULL DAY RATE')], max_length=40)),
                ('location', models.CharField(max_length=30)),
                ('duration', models.CharField(max_length=30)),
                ('addedOn', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField()),
                ('project', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Freelancing.project')),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='skills',
            field=models.ManyToManyField(to='Freelancing.skill'),
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=20)),
                ('zipCode', models.IntegerField()),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('address', models.CharField(max_length=50)),
                ('customerAddress', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Freelancing.customer')),
            ],
        ),
    ]
