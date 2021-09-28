# Generated by Django 2.2 on 2019-10-23 21:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('commandes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commande',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='commande',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='commande',
            name='updated',
        ),
        migrations.AddField(
            model_name='commande',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]