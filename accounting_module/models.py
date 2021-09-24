from django.db import models
from django.db.models.deletion import CASCADE

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

class JournalEntry(models.Model):
    transdate = models.DateField()
    journal = models.CharField(max_length=100)
    reference = models. CharField(max_length=100)
    check_no_ref = models.CharField(max_length=100)
    journalMemo = models.CharField(max_length=500)
    code = models.CharField(max_length=30)
    trialBalance_chart = models.CharField(max_length=100)
    account_name = models.ForeignKey(ChartofAccount,
                                            on_delete=models.CASCADE)
    debit = models.DecimalField(max_digits=19,decimal_places=2)   
    credit = models.DecimalField(max_digits=19,decimal_places=2)  
    update = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)                                 




