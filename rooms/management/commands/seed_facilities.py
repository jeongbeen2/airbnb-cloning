from rooms.models import Amenity, Facility
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    help = "This command creates a lot of facilities"

    """     def add_arguments(self, parser):
        parser.add_argument(
            "--times",
            help="How many times?",
        ) """

    def handle(self, *args, **options):
        facilities = [
            "Private entrance",
            "Paid parking on premises",
            "Paid parking off premises",
            "Elevator",
            "Parking",
            "Gym",
        ]

        for f in facilities:
            Facility.objects.create(name=f)
        self.stdout.write(self.style.SUCCESS(f"{len(facilities)} Facilities created!"))