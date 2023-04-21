from django.contrib import admin

from money.models import Transaction, Tag
# Register your models here.

admin.site.register(Transaction)
admin.site.register(Tag)