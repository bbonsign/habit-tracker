# Generated by Django 3.0.4 on 2020-03-06 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20200305_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='achievement',
            field=models.PositiveIntegerField(default=0, help_text='How much/many times did you do your habit?'),
        ),
    ]
