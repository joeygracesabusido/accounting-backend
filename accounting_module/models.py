from django.db import models

# Create your models here.

class ChartofAccount(models.Model):
    balanceSheet_type = (
        ('CA','Current Asset'),
        ('NCA','Non-Current Asset'),
        ('CL','Current Liability'),
        ('NCL','Non-Current Liability'),
        ('E','Equity'),
        ('I','Income'),
        ('EXCOS','Cost OF Sale Expense'),
        ('EXGA','General and Adminimistrative Expense')
    )
    trialBalance_chart = models.CharField(max_length=100)
    account_name = models.CharField(max_length=100)
    code =  models.CharField(max_length=100)

    def __str__(self):
        return "%s %s" % (self.trialBalance_chart, self.account_name)

    class Meta:
        ordering = ['account_name']

