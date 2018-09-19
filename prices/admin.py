from django.contrib import admin

from .models import Candle, Trade


admin.site.register(Candle)
admin.site.register(Trade)
