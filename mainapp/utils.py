from mainapp.models import Candidate, Ballot, TITLES


def add_voter_count(obj):
    candidates = Candidate.objects.all()
    c1 = candidates.get(name=obj.tru1, title="tru")
    c1.add_count()
    c1.save(update_fields=["count"])
    c2 = candidates.get(name=obj.tru2, title="tru")
    c2.add_count()
    c2.save(update_fields=["count"])
    c3 = candidates.get(name=obj.tru3, title="tru")
    c3.add_count()
    c3.save(update_fields=["count"])
    titles = [i[0] for i in TITLES]
    for title, name in obj.__dict__.items():
        if title in titles:
            q = {"title": title, "name": name}
            c = candidates.get(**q)
            c.add_count()
            c.save(update_fields=["count"])
    return True
