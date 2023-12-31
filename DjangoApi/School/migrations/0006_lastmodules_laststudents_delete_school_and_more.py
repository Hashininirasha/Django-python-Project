# Generated by Django 4.2.6 on 2023-10-17 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('School', '0005_schools_remove_newstudents_modules_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='LastModules',
            fields=[
                ('Name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('duration', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='LastStudents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('modules', models.ManyToManyField(to='School.lastmodules')),
            ],
        ),
        migrations.DeleteModel(
            name='School',
        ),
        migrations.RemoveField(
            model_name='students',
            name='modules',
        ),
        migrations.DeleteModel(
            name='Modules',
        ),
        migrations.DeleteModel(
            name='Students',
        ),
    ]
