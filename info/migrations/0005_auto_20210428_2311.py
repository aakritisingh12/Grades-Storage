# Generated by Django 3.2 on 2021-04-28 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0004_auto_20210428_2210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marks',
            name='name',
            field=models.CharField(choices=[('LAB 1', 'LAB 1'), ('LAB 2', 'LAB 2'), ('LAB 3', 'LAB 3'), ('LAB 4', 'LAB 4'), ('LAB 5', 'LAB 5'), ('LAB 6', 'LAB 6'), ('LAB 7', 'LAB 7'), ('Assignment 1', 'Assignment 1'), ('Assignment 2', 'Assignment 2'), ('MID SEM', 'MID SEM'), ('Project', 'Project'), ('Semester End Exam', 'Semester End Exam')], default='LAB 1', max_length=50),
        ),
        migrations.AlterField(
            model_name='marksclass',
            name='name',
            field=models.CharField(choices=[('LAB 1', 'LAB 1'), ('LAB 2', 'LAB 2'), ('LAB 3', 'LAB 3'), ('LAB 4', 'LAB 4'), ('LAB 5', 'LAB 5'), ('LAB 6', 'LAB 6'), ('LAB 7', 'LAB 7'), ('Assignment 1', 'Assignment 1'), ('Assignment 2', 'Assignment 2'), ('MID SEM', 'MID SEM'), ('Project', 'Project'), ('Semester End Exam', 'Semester End Exam')], default='LAB 1', max_length=50),
        ),
        migrations.DeleteModel(
            name='AssignTime',
        ),
    ]