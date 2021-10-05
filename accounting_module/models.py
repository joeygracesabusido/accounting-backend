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
        return self.account_name
        # return "%s %s" % (self.trialBalance_chart, self.account_name)

    class Meta:
        ordering = ['account_name']

class JournalEntry(models.Model):
    transdate = models.DateField(null=True, blank=True)
    journal = models.CharField(max_length=100,null=True, blank=True)
    reference = models. CharField(max_length=100,null=True, blank=True)
    check_no_ref = models.CharField(max_length=100,null=True, blank=True)
    journalMemo = models.CharField(max_length=500,null=True, blank=True)
    account_name_id = models.ForeignKey(ChartofAccount, related_name='marks',
                                             null=True, blank=True,
                                            on_delete=models.CASCADE)
    # account_name =  models.CharField(max_length=500,null=True, blank=True)
    # debit = models.DecimalField(max_digits=19,decimal_places=2,null=True, blank=True)   
    # credit = models.DecimalField(max_digits=19,decimal_places=2,null=True, blank=True) 
    debit = models.CharField(max_length=500,null=True, blank=True)   
    credit = models.CharField(max_length=500,null=True, blank=True) 
    update = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)                                 




