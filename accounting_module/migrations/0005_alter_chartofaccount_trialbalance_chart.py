# Generated by Django 3.2.7 on 2021-09-23 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting_module', '0004_alter_chartofaccount_trialbalance_chart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chartofaccount',
            name='trialBalance_chart',
            field=models.CharField(choices=[('CA', 'Current Asset'), ('NCA', 'Non-Current Asset'), ('CL', 'Current Liability'), ('NCL', 'Non-Current Liability'), ('E', 'Equity'), ('I', 'Income'), ('EXCOS', 'Cost OF Sale Expense'), ('EXGA', 'General and Adminimistrative Expense')], max_length=100),
        ),
    ]
