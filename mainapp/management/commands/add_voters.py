import argparse

from django.core.management.base import BaseCommand
import csv

from mainapp.models import User, Voter


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("--file", type=argparse.FileType("r"))

    def handle(self, *args, **options):
        voter_file = options["file"]
        csvreader = csv.reader(voter_file)
        header = next(csvreader)
        count = 0
        for row in csvreader:
            user, _ = User.objects.get_or_create(email=row[1])
            Voter.objects.get_or_create(name=row[0], user=user)
            count += 1
        self.stdout.write(self.style.SUCCESS(count))
        self.stdout.write(self.style.SUCCESS("Success"))
