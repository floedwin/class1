# Generated by Django 2.2.1 on 2019-05-29 10:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('marks', '0004_auto_20190524_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marks',
            name='student_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='marks', to='marks.Student'),
        ),
    ]