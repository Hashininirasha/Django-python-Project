# Generated by Django 4.2.6 on 2023-10-17 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('School', '0015_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('Subject_Id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('Subject', models.CharField(max_length=200)),
                ('Subject_score', models.FloatField()),
            ],
        ),
    ]
