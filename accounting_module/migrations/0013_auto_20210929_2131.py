# Generated by Django 3.2.7 on 2021-09-29 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting_module', '0012_auto_20210929_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journalentry',
            name='credit',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='journalentry',
            name='debit',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
