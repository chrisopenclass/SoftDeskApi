# Generated by Django 4.0.4 on 2022-06-24 22:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_alter_contributor_role'),
    ]

    operations = [
        migrations.RenameField(
            model_name='issue',
            old_name='desc',
            new_name='description',
        ),
    ]
