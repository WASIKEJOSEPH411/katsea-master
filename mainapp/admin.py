from django.contrib import admin

# Register your models here.
from .models import Voter, Ballot, User, Candidate, VotingTime

admin.site.register(Voter)

admin.site.register(Ballot)

admin.site.register(User)

admin.site.register(Candidate)

admin.site.register(VotingTime)
