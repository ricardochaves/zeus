from django.core.management.base import BaseCommand

from olympus.models import SystemUser


class Command(BaseCommand):
    help = "Seed database"

    def handle(self, *args, **options):
        SystemUser.objects.create(
            first_name="Ricardo", last_name="Chaves", email="ricardobchaves6@gmail.com"
        )
