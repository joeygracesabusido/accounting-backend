# Generated by Django 3.2.7 on 2021-10-06 07:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounting_module', '0027_remove_journalentry_account_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='journalentry',
            old_name='account_name_id',
            new_name='account_name',
        ),
    ]
