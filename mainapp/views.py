from django.shortcuts import render, redirect, HttpResponse
from .models import Voter, Ballot, User, Candidate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib import messages
from mainapp.utils import add_voter_count


# Create your views here.


@login_required(login_url="login")
def home(request):
    voter = request.user.voter
    if voter.status is True:
        return render(
            request,
            "mainapp/success.html",
            {"msg": "You already voted"},
        )
    candidates = Candidate.objects.values("name", "title")
    if request.method == "POST":
        b = Ballot.objects.create(
            voter=voter,
            pr=request.POST.get("pr"),
            vp=request.POST.get("vp"),
            sg=request.POST.get("sg"),
            vs=request.POST.get("vs"),
            tr=request.POST.get("tr"),
            dt=request.POST.get("dt"),
            os=request.POST.get("os"),
            eas=request.POST.get("eas"),
            ers=request.POST.get("ers"),
            ad=request.POST.get("ad"),
            tru1=request.POST.getlist("tru")[0],
            tru2=request.POST.getlist("tru")[1],
            tru3=request.POST.getlist("tru")[2],
        )
        add_voter_count(b)
        voter.status = True
        voter.save(update_fields=["status"])
        logout(request)
        return render(
            request, "mainapp/success.html", {"msg": "Thanks for voting"}
        )
    return render(
        request, "mainapp/home.html", {"voter": voter, "candidates": candidates}
    )


# @login_required(login_url='login')
def report(request):
    ballots = Ballot.objects.select_related("voter")
    context = {"ballots": ballots}
    return render(request, "mainapp/report.html", context)


def vote_count(request):
    candidates = Candidate.objects.all().order_by("-count")
    voters = Voter.objects.all()
    voted = f"{voters.filter(status=True).count()} / {voters.count()} voters"
    return render(
        request,
        "mainapp/vote_count.html",
        {"candidates": candidates, "voted": voted},
    )


def signin(request):
    if request.method == "POST":
        code = request.POST.get("code").strip()
        voter = Voter.objects.filter(code=code)
        if voter.exists():
            v = voter[0]
            if v.status == True:
                return render(
                    request,
                    "mainapp/success.html",
                    {"msg": "You already voted"},
                )
            user = User.objects.get(voter=v)
            login(request, user)
            return redirect("home")
        messages.warning(request, "Invalid code try again")
    return render(request, "mainapp/login.html", {})


def blank(request):
    return HttpResponse("Election not Active")
