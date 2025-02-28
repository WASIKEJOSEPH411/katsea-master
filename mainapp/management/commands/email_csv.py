from django.core.management.base import BaseCommand
from mainapp.models import Voter
import csv


class Command(BaseCommand):
    help = "Send voting Codes Email"

    def add_arguments(self, parser):
        parser.add_argument("--email", type=str)

    def handle(self, *args, **options):
        voters = Voter.objects.all()
        email = options["email"]
        if email:
            voters = voters.filter(user__email=email).all()
        rows = []
        for voter in voters:
            rows.append(
                [
                    voter.user.email,
                    voter.name,
                    voter.code
                ]
            )
        with open("voter_codes.csv", "w", encoding="UTF8") as f:
            writer = csv.writer(f)
            writer.writerows(rows)
        self.stdout.write(self.style.SUCCESS("Success"))
