from django.contrib import admin
from auction.models import User, Cat, Hedgehog, Lot, Bid, Item


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    pass


@admin.register(Cat)
class CatAdmin(admin.ModelAdmin):
    pass


@admin.register(Hedgehog)
class HedgehogAdmin(admin.ModelAdmin):
    pass


@admin.register(Lot)
class LotAdmin(admin.ModelAdmin):
    pass


@admin.register(Bid)
class BidAdmin(admin.ModelAdmin):
    pass
