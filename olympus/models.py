import uuid

from django.db import models

# Create your models here.


class SystemUser(models.Model):
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Create at")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Update at")
    first_name = models.CharField(max_length=30, verbose_name="First Name")
    last_name = models.CharField(max_length=30, verbose_name="Last Name")
    email = models.EmailField(verbose_name="E-mail")

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = "System User"
        verbose_name_plural = "System Users"


class Customer(models.Model):
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Create at")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Update at")
    name = models.CharField(max_length=200, verbose_name="Name")
    email = models.EmailField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"


class Track(models.Model):
    TRACK_TYPES = (
        (1, "Resgate"),
        (2, "Transferencia"),
        (3, "Estorno"),
        (4, "Repasse Indústria"),
        (5, "Promoções"),
        (6, "Expirado"),
    )

    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Create at")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Update at")
    identifier = models.UUIDField(default=uuid.uuid4, editable=False, verbose_name="Identify")
    track_type = models.IntegerField(choices=TRACK_TYPES, verbose_name="Type")

    def __str__(self):
        return str(self.track_type)

    class Meta:
        verbose_name = "Track"
        verbose_name_plural = "Tracks"


class Consumption(models.Model):
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Create at")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Update at")
    track = models.ForeignKey(Track, on_delete=models.CASCADE, verbose_name="Track")
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name="Customer")
    points = models.IntegerField(verbose_name="Points")

    def __str__(self):
        return str(self.customer)

    class Meta:
        verbose_name = "Consumption"
        verbose_name_plural = "Consumptions"


class Expired(models.Model):
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Create at")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Update at")
    track = models.ForeignKey(Track, on_delete=models.CASCADE, verbose_name="Track")
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name="Customer")
    points = models.IntegerField(verbose_name="Points")

    def __str__(self):
        return str(self.customer)

    class Meta:
        verbose_name = "Expired"
        verbose_name_plural = "Expireds"


class Transfer(models.Model):
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Create at")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Update at")
    track = models.ForeignKey(Track, on_delete=models.CASCADE, verbose_name="Track")
    customer_origen = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name="TransferOrigen",
        verbose_name="Customer Origen",
    )
    customer_destination = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name="TransferDestination",
        verbose_name="Customer Destination",
    )
    points = models.IntegerField(verbose_name="Points")

    def __str__(self):
        return f"{self.customer_origen} to {self.customer_destination}"

    class Meta:
        verbose_name = "Transfer"
        verbose_name_plural = "Transfers"


class PointsReversal(models.Model):
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Create at")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Update at")
    track = models.ForeignKey(
        Track, on_delete=models.CASCADE, related_name="Track", verbose_name="Track"
    )
    reversed_tracking = models.ForeignKey(
        Track, on_delete=models.CASCADE, related_name="ReversedTracking", verbose_name="Track"
    )
    points = models.IntegerField(verbose_name="Points")

    def __str__(self):
        return f"Reversed: {self.reversed_tracking}"

    class Meta:
        verbose_name = "Point Reversal"
        verbose_name_plural = "Points Reversal"


class Industry(models.Model):
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Create at")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Update at")
    name = models.CharField(max_length=200, verbose_name="Name")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Industry"
        verbose_name_plural = "Industrys"


class IndustrialRepass(models.Model):
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Create at")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Update at")
    track = models.ForeignKey(Track, on_delete=models.CASCADE, verbose_name="Track")
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name="Customer")
    points = models.IntegerField(verbose_name="Points")
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE, verbose_name="Indústria")

    def __str__(self):
        return str(self.customer)

    class Meta:
        verbose_name = "Industrial Repass"
        verbose_name_plural = "Industrial Repasses"


class Contract(models.Model):
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Create at")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Update at")
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE, verbose_name="Industry")

    start_date = models.DateField(verbose_name="Start Date")
    end_date = models.DateField(verbose_name="End Date")

    def __str__(self):
        return f"{self.id} - {self.industry}"

    class Meta:
        verbose_name = "Contract"
        verbose_name_plural = "Contracts"


class TierType(models.Model):
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Create at")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Update at")
    name = models.CharField(max_length=200, verbose_name="Name")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Tier Type"
        verbose_name_plural = "Tier Types"


class Tier(models.Model):
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Create at")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Update at")
    tier_type = models.ForeignKey(TierType, on_delete=models.CASCADE, verbose_name="Tier Type")

    contract = models.ForeignKey(Contract, on_delete=models.CASCADE, verbose_name="Contrato")

    points = models.IntegerField(verbose_name="Points")
    used_points = models.IntegerField(verbose_name="Used Points")
    days_before_expiration = models.IntegerField(
        verbose_name="Days Before Expiration",
        help_text="Total de dias que vai expirar quando o usuário ganhar os pontos",
    )
    order = models.IntegerField(verbose_name="Order")
    point_value = models.DecimalField(max_digits=10, decimal_places=4, verbose_name="Point Value")

    def __str__(self):
        return f"{self.id} - {self.tier_type}"

    class Meta:
        verbose_name = "Tier"
        verbose_name_plural = "Tiers"


class PromotionRepass(models.Model):
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Create at")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Update at")
    track = models.ForeignKey(Track, on_delete=models.CASCADE, verbose_name="Track")
    promotion = models.IntegerField(verbose_name="Promotion")  # vai virar FK
    points = models.IntegerField(verbose_name="Points")
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name="Customer")

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = "Pomotion Repass"
        verbose_name_plural = "Pomotion Repasses"


class CustomerTier(models.Model):
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Create at")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Update at")
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name="Customer")
    tier = models.ForeignKey(Tier, on_delete=models.CASCADE, verbose_name="Tier")
    track = models.ForeignKey(Track, on_delete=models.CASCADE, verbose_name="Track")
    points = models.IntegerField(verbose_name="Points")
    point_expired_date = models.DateTimeField(verbose_name="Point Exipred Date")
    used_points = models.IntegerField(verbose_name="Used Points")

    def __str__(self):
        return f"{self.customer}"

    class Meta:
        verbose_name = "Customer Tier"
        verbose_name_plural = "Customers Tier"


class CustomerTierUsed(models.Model):
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Create at")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Update at")
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name="Customer")
    customer_tier = models.ForeignKey(
        CustomerTier, on_delete=models.CASCADE, verbose_name="Customer Tier"
    )
    track = models.ForeignKey(Track, on_delete=models.CASCADE, verbose_name="Track")
    points = models.IntegerField(verbose_name="Points")

    def __str__(self):
        return str(self.customer)

    class Meta:
        verbose_name = "Customer Tier Used"
        verbose_name_plural = "Customers Tier Used"
