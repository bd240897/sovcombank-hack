from django.contrib import admin
from .models import Data
from .models import Profile, Currency, CurrencyCourse, Wallet, Transfer


@admin.register(Data)
class DataAdmin(admin.ModelAdmin):
    pass


admin.site.register(Profile)
admin.site.register(Currency)
admin.site.register(CurrencyCourse)
admin.site.register(Wallet)
admin.site.register(Transfer)
