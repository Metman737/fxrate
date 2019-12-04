from django.contrib import admin

# Register your models here.
from home.models import Post, Currency, ExchangeRate

admin.site.register(Post)
admin.site.register(Currency)
admin.site.register(ExchangeRate)
