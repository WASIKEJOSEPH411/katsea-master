from django.core.management.base import BaseCommand
from mainapp.models import Voter
from django.core.mail import send_mass_mail


class Command(BaseCommand):
    help = "Send voting Codes Email"

    def add_arguments(self, parser):
        parser.add_argument("--email", type=str)

    def handle(self, *args, **options):
        voters = Voter.objects.all()
        email = options["email"]
        if email:
            voters = voters.filter(user__email=email).all()
        message = []
        for voter in voters:
            m = (
                "KATSEA Election 1st April 2023 Voting Code",
                f"Dear {voter.name}, \n\nVoting code:\n{voter.code} \n\nVoting link:\nhttps://katsea.herokuapp.com/\n\nKind regards,\nDaniel Kakai",
                "Election Administrator <admin@katsea.co.ke>",
                [voter.user.email],
            )
            message.append(m)
            print(voter.user.email)
        send_mass_mail(message, fail_silently=False)
        self.stdout.write(self.style.SUCCESS("Success"))
