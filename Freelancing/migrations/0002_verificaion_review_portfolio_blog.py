# Generated by Django 4.0.5 on 2022-06-13 07:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Freelancing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Verificaion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yourName', models.CharField(max_length=30)),
                ('contactNumber', models.IntegerField()),
                ('passport', models.CharField(max_length=30)),
                ('document', models.FileField(upload_to='verification/')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Freelancing.address')),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Freelancing.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('rating', models.IntegerField()),
                ('description', models.TextField()),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Freelancing.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('link', models.URLField()),
                ('files', models.FileField(upload_to='Files/')),
                ('description', models.TextField()),
                ('customer', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Freelancing.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('posted_on', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Freelancing.customer')),
            ],
        ),
    ]
