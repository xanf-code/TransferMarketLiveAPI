from django.core.management.base import BaseCommand
from transfermktAPI.models import Transfer

class Command(BaseCommand):
    def handle(self, *args, **options):
        Transfer.objects.all().delete()