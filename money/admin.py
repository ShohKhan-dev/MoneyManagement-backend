from django.contrib import admin

from money.models import Transaction, Tag, User
# Register your models here.

admin.site.register(User)
admin.site.register(Transaction)
admin.site.register(Tag)
