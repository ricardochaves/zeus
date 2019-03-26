from django.contrib import admin

from olympus.models import Consumption
from olympus.models import Contract
from olympus.models import Customer
from olympus.models import CustomerTier
from olympus.models import CustomerTierUsed
from olympus.models import Expired
from olympus.models import IndustrialRepass
from olympus.models import Industry
from olympus.models import PointsReversal
from olympus.models import PromotionRepass
from olympus.models import SystemUser
from olympus.models import Tier
from olympus.models import TierType
from olympus.models import Track
from olympus.models import Transfer

# Register your models here.


@admin.register(SystemUser)
class SystemUserAdmin(admin.ModelAdmin):
    date_hierarchy = "create_at"
    list_display = ("first_name", "create_at")


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    date_hierarchy = "create_at"
    list_display = ("industry", "start_date", "end_date", "create_at")


@admin.register(Consumption)
class ConsumptionAdmin(admin.ModelAdmin):
    date_hierarchy = "create_at"
    list_display = ("customer", "points", "create_at")


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    date_hierarchy = "create_at"
    list_display = ("name", "create_at")


@admin.register(CustomerTier)
class CustomerTierAdmin(admin.ModelAdmin):
    date_hierarchy = "create_at"
    list_display = ("customer", "tier", "points", "create_at")


@admin.register(CustomerTierUsed)
class CustomerTierUsedAdmin(admin.ModelAdmin):
    date_hierarchy = "create_at"
    list_display = ("customer", "points", "create_at")


@admin.register(Expired)
class ExpiredAdmin(admin.ModelAdmin):
    date_hierarchy = "create_at"
    list_display = ("customer", "points", "create_at")


@admin.register(IndustrialRepass)
class IndustrialRepassAdmin(admin.ModelAdmin):
    date_hierarchy = "create_at"
    list_display = ("customer", "industry", "points", "create_at")


@admin.register(Industry)
class IndustryAdmin(admin.ModelAdmin):
    date_hierarchy = "create_at"
    list_display = ("name", "create_at")


@admin.register(PointsReversal)
class PointsReversalAdmin(admin.ModelAdmin):
    date_hierarchy = "create_at"
    list_display = ("reversed_tracking", "create_at")


@admin.register(PromotionRepass)
class PromotionRepassAdmin(admin.ModelAdmin):
    date_hierarchy = "create_at"
    list_display = ("promotion", "points", "create_at")


@admin.register(Tier)
class TierAdmin(admin.ModelAdmin):
    date_hierarchy = "create_at"
    list_display = (
        "tier_type",
        "contract",
        "points",
        "used_points",
        "create_at",
        "point_value",
        "order",
    )


@admin.register(TierType)
class TierTypeAdmin(admin.ModelAdmin):
    date_hierarchy = "create_at"
    list_display = ("name", "create_at")


@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    date_hierarchy = "create_at"
    list_display = ("identifier", "track_type", "create_at")


@admin.register(Transfer)
class TransferAdmin(admin.ModelAdmin):
    date_hierarchy = "create_at"
    list_display = ("customer_origen", "customer_destination", "points", "create_at")


# @admin.register(CheckingAccount)
# class CheckingAccountAdmin(admin.ModelAdmin):
#     date_hierarchy = "create_at"
#     list_display = ("client", "bank", "number", "create_at")
#     list_filter = ("client", "bank", "create_at")
#     search_fields = ["number"]


# @admin.register(Client)
# class ClientAdmin(admin.ModelAdmin):
#     date_hierarchy = "create_at"
#     list_display = ("name", "create_at")
#     list_filter = ("name", "create_at")


# @admin.register(Bank)
# class BankAdmin(admin.ModelAdmin):
#     date_hierarchy = "create_at"
#     list_display = ("name", "create_at")
#     list_filter = ("name", "create_at")
#     search_fields = ["name"]


# @admin.register(BankLot)
# class BankLotAdmin(admin.ModelAdmin):
#     date_hierarchy = "create_at"
#     list_display = ("bank", "create_at")
#     list_filter = ("bank", "create_at")


# @admin.register(EntryType)
# class EntryTypeAdmin(admin.ModelAdmin):
#     date_hierarchy = "create_at"
#     list_display = ("name", "create_at")
#     list_filter = ("name", "create_at")


# @admin.register(Entry)
# class EntryAdmin(admin.ModelAdmin):
#     date_hierarchy = "create_at"
#     list_display = ("client", "bank", "entry_type", "value", "create_at")
#     list_filter = ("client", "entry_type", "bank", "create_at")
#     ordering = ("create_at",)
