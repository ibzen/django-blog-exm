# Generated by Django 4.0.2 on 2022-02-21 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=255, verbose_name='Firstname')),
                ('lastname', models.CharField(max_length=255, verbose_name='Lastname')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('status', models.BooleanField(default=True, verbose_name='Author status')),
                ('creation_date', models.DateField(auto_now_add=True, verbose_name='Creation Date')),
                ('facebook', models.URLField(blank=True, null=True, verbose_name='Facebook author')),
                ('twitter', models.URLField(blank=True, null=True, verbose_name='Twitter author')),
                ('instagram', models.URLField(blank=True, null=True, verbose_name='Instagram author')),
                ('website', models.URLField(blank=True, null=True, verbose_name='Website author')),
            ],
            options={
                'verbose_name': 'Author',
                'verbose_name_plural': 'Authors',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Category Name')),
                ('status', models.BooleanField(default=True, verbose_name='Category status')),
                ('creation_date', models.DateField(auto_now_add=True, verbose_name='Creation Date')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ['name'],
            },
        ),
    ]
