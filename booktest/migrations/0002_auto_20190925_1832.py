# Generated by Django 2.2.5 on 2019-09-25 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookinfo',
            old_name='bititle',
            new_name='btitle',
        ),
    ]
