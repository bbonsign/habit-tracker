# Generated by Django 3.0.4 on 2020-03-07 19:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0015_auto_20200307_0215'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='log',
            name='unique_record',
        ),
        migrations.AlterField(
            model_name='log',
            name='habit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logs', to='core.Habit'),
        ),
        migrations.AlterField(
            model_name='log',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logs', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddConstraint(
            model_name='log',
            constraint=models.UniqueConstraint(fields=('date', 'habit', 'owner'), name='unique_log'),
        ),
    ]
