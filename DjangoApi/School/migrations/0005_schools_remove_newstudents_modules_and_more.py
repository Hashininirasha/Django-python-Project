# Generated by Django 4.2.6 on 2023-10-17 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('School', '0004_onenewstudents'),
    ]

    operations = [
        migrations.CreateModel(
            name='schools',
            fields=[
                ('School_Id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('Sch_Name', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='newstudents',
            name='modules',
        ),
        migrations.RemoveField(
            model_name='onenewstudents',
            name='module',
        ),
        migrations.DeleteModel(
            name='NewModules',
        ),
        migrations.DeleteModel(
            name='NewStudents',
        ),
        migrations.DeleteModel(
            name='OneNewStudents',
        ),
    ]