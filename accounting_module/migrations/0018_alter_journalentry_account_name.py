# Generated by Django 3.2.7 on 2021-10-05 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting_module', '0017_alter_journalentry_account_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journalentry',
            name='account_name',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
