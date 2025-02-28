from django.core.management.base import BaseCommand, CommandError
from mainapp.models import Voter, Candidate, Ballot


class Command(BaseCommand):
    help = "Reset voting status"

    def handle(self, *args, **options):
        Voter.objects.update(status=False)
        Candidate.objects.update(count=0)
        Ballot.objects.all().delete()
        self.stdout.write(self.style.SUCCESS("Success"))
