from django.contrib import admin

# Register your models here.

from .models import ChartofAccount, JournalEntry

admin.site.register(ChartofAccount)
admin.site.register(JournalEntry)
