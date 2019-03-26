from datetime import datetime
from datetime import timedelta

from django.core.management.base import BaseCommand

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


class Command(BaseCommand):
    help = "Seed database"

    def handle(self, *args, **options):
        SystemUser.objects.create(
            first_name="Ricardo", last_name="Chaves", email="ricardobchaves6@gmail.com"
        )

        customer_ricardo = Customer.objects.create(name="Ricardo")
        customer_igor = Customer.objects.create(name="Igor")
        customer_william = Customer.objects.create(name="William")
        customer_danny = Customer.objects.create(name="Danny")

        tier_contrato = TierType.objects.create(name="Contrato")
        tier_infinito = TierType.objects.create(name="Infinito")
        tier_promocao_natal = TierType.objects.create(name="Promoção de Natal")

        industria_votoram = Industry.objects.create(name="Votorantim")
        industria_tigre = Industry.objects.create(name="Tigre")

        # Criamos contrato
        contrato_vc = Contract.objects.create(
            industry=industria_votoram,
            start_date=datetime.now(),
            end_date=datetime.now() + timedelta(days=1),
        )

        # Criou os Tiers
        tier_contract_1 = Tier.objects.create(
            contract=contrato_vc,
            tier_type=tier_contrato,
            points=1_000_000,
            days_before_expiration=365,
            order=1,
            point_value=0.12,
            used_points=0,
        )

        tier_contract_2 = Tier.objects.create(
            contract=contrato_vc,
            tier_type=tier_contrato,
            points=200_000,
            days_before_expiration=365,
            order=2,
            point_value=0.1,
            used_points=0,
        )

        tier_contract_3 = Tier.objects.create(
            contract=contrato_vc,
            tier_type=tier_promocao_natal,
            points=50000,
            days_before_expiration=30,
            order=1,
            point_value=0.04,
            used_points=0,
        )

        # Repasse da Indústria
        track_1 = Track.objects.create(track_type=4)
        repasse_1 = IndustrialRepass.objects.create(
            points=100, track=track_1, customer=customer_ricardo, industry=industria_votoram
        )
        CustomerTier.objects.create(
            customer=customer_ricardo,
            tier=tier_contract_1,
            track=track_1,
            points=100,
            point_expired_date=datetime.now() + timedelta(days=365),
            used_points=0,
        )

        track_2 = Track.objects.create(track_type=4)
        repasse_2 = IndustrialRepass.objects.create(
            points=1000, track=track_2, customer=customer_igor, industry=industria_votoram
        )
        custumer_tier_igor_1 = CustomerTier.objects.create(
            customer=customer_igor,
            tier=tier_contract_1,
            track=track_2,
            points=500,
            point_expired_date=datetime.now() + timedelta(days=365),
            used_points=0,
        )
        custumer_tier_igor_2 = CustomerTier.objects.create(
            customer=customer_igor,
            tier=tier_contract_2,
            track=track_2,
            points=500,
            point_expired_date=datetime.now() + timedelta(days=365),
            used_points=0,
        )

        # Criar um resgate
        track_3 = Track.objects.create(track_type=1)
        Consumption.objects.create(track=track_3, customer=customer_igor, points=600)

        CustomerTierUsed.objects.create(
            customer_tier=custumer_tier_igor_1, customer=customer_igor, track=track_3, points=500
        )
        custumer_tier_igor_1.used_points = 500
        custumer_tier_igor_1.save()

        CustomerTierUsed.objects.create(
            customer_tier=custumer_tier_igor_2, customer=customer_igor, track=track_3, points=100
        )
        custumer_tier_igor_2.used_points = 100
        custumer_tier_igor_2.save()

        # Estorno

        track_4 = Track.objects.create(track_type=3)
        PointsReversal.objects.create(reversed_tracking=track_3, track=track_4, points=200)

        custumer_tier_igor_2.used_points = (
            custumer_tier_igor_2.used_points - 100
        )  # não ficar negativo é em outro momento

        custumer_tier_igor_1.used_points = (
            custumer_tier_igor_1.used_points - 100
        )  # não ficar negativo é em outro momento

        # Promoção
        track_5 = Track.objects.create(track_type=5)
        PromotionRepass.objects.create(
            track=track_5, promotion=1, points=700, customer=customer_igor
        )

        custumer_tier_igor_3 = CustomerTier.objects.create(
            customer=customer_igor,
            tier=tier_contract_3,  # promossional de natal
            track=track_5,
            points=700,
            point_expired_date=datetime.now() + timedelta(days=60),
            used_points=0,
        )

        # Transferencia
        track_6 = Track.objects.create(track_type=2)

        Transfer.objects.create(
            track=track_6,
            customer_origen=customer_igor,
            customer_destination=customer_ricardo,
            points=300,
        )

        custumer_tier_ricardo_1 = CustomerTier.objects.create(
            customer=customer_ricardo,
            tier=tier_contract_1,
            track=track_6,
            points=300,
            point_expired_date=datetime.now() + timedelta(days=365),
            used_points=0,
        )

        CustomerTierUsed.objects.create(
            customer_tier=custumer_tier_igor_1, customer=customer_igor, track=track_6, points=300
        )

        # Expired

        track_7 = Track.objects.create(track_type=6)
        Expired.objects.create(track=track_7, customer=customer_igor, points=200)
        CustomerTierUsed.objects.create(
            customer_tier=custumer_tier_igor_1, customer=customer_igor, track=track_7, points=200
        )
