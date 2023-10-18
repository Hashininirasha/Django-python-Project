# Generated by Django 4.2.6 on 2023-10-17 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('School', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Modules',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('duration', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('modules', models.ManyToManyField(to='School.modules')),
            ],
        ),
    ]
