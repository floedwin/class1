# Generated by Django 2.2.1 on 2019-05-04 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_number', models.IntegerField(db_index=True, max_length=20, unique=True, verbose_name='student_number')),
                ('math', models.CharField(default='', max_length=10, verbose_name='math')),
                ('english', models.IntegerField(default='', max_length=20, verbose_name='english')),
                ('agric', models.IntegerField(default='', max_length=10, verbose_name='agric')),
                ('bio', models.IntegerField(default='', max_length=10, verbose_name='bio')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_number', models.IntegerField(db_index=True, max_length=20, unique=True, verbose_name='student_number')),
                ('student_name', models.CharField(default='', max_length=200, verbose_name='student_name')),
                ('gender', models.CharField(default='', max_length=20, verbose_name='gender')),
                ('age', models.IntegerField(default='', max_length=10, verbose_name='age')),
            ],
        ),
    ]
