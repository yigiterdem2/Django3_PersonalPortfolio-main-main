# Generated by Django 5.0.6 on 2024-05-26 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='title',
            old_name='baslik',
            new_name='head',
        ),
        migrations.RenameField(
            model_name='title',
            old_name='aciklama',
            new_name='opening',
        ),
    ]
