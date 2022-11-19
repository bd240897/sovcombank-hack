from django.contrib import admin
from .models import Data, Profile, Currency, CurrencyCourse, Wallet, Transfer

@admin.register(Data)
class DataAdmin(admin.ModelAdmin):
    pass

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass

@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    pass

@admin.register(CurrencyCourse)
class CurrencyCourseAdmin(admin.ModelAdmin):
    pass

@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    pass

@admin.register(Transfer)
class TransferAdmin(admin.ModelAdmin):
    pass
