from django.core.management.base import BaseCommand
from mainapp.models import Voter


class Command(BaseCommand):
    help = "Generate voting codes"

    def add_arguments(self, parser):
        parser.add_argument("--email", type=str)

    def handle(self, *args, **options):
        voters = Voter.objects.all()
        email = options["email"]
        if email:
            voters = voters.filter(user__email=email).all()
        for voter in voters:
            voter.generate_code()
            voter.save()
        self.stdout.write(self.style.SUCCESS("Success"))
