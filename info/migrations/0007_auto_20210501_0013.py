# Generated by Django 3.2 on 2021-04-30 18:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0006_auto_20210429_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dept',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='marks',
            name='name',
            field=models.CharField(choices=[('LAB 1', 'LAB 1'), ('LAB 2', 'LAB 2'), ('LAB 3', 'LAB 3'), ('LAB 4', 'LAB 4'), ('LAB 5', 'LAB 5'), ('LAB 6', 'LAB 6'), ('LAB 7', 'LAB 7'), ('Assignment 1', 'Assignment 1'), ('Assignment 2', 'Assignment 2'), ('Mid Sem', 'Mid Sem'), ('Project', 'Project'), ('End Sem', 'End Sem')], default='LAB 1', max_length=50),
        ),
        migrations.AlterField(
            model_name='marksclass',
            name='name',
            field=models.CharField(choices=[('LAB 1', 'LAB 1'), ('LAB 2', 'LAB 2'), ('LAB 3', 'LAB 3'), ('LAB 4', 'LAB 4'), ('LAB 5', 'LAB 5'), ('LAB 6', 'LAB 6'), ('LAB 7', 'LAB 7'), ('Assignment 1', 'Assignment 1'), ('Assignment 2', 'Assignment 2'), ('Mid Sem', 'Mid Sem'), ('Project', 'Project'), ('End Sem', 'End Sem')], default='LAB 1', max_length=50),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
