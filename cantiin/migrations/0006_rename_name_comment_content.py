# Generated by Django 3.2.4 on 2021-06-30 10:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cantiin', '0005_auto_20210630_0130'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='name',
            new_name='content',
        ),
    ]