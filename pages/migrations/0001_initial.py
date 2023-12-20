# Generated by Django 5.0 on 2023-12-18 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MainScrollModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='main-scroll')),
                ('title', models.CharField(max_length=50)),
                ('info', models.CharField(max_length=255)),
                ('discount', models.PositiveSmallIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'scroll',
                'verbose_name_plural': 'scrolls',
            },
        ),
    ]
