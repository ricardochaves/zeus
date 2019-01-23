from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Create a super user"

    def handle(self, *args, **options):
        u = User(username="admin")
        u.set_password("test")
        u.is_superuser = True
        u.is_staff = True
        u.save()
