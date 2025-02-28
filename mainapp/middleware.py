from django.utils import timezone

from mainapp.views import blank

from mainapp.models import VotingTime


def time_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        if (
                "admin" in request.path
                or "report" in request.path
                or "vote-count" in request.path
        ):
            return get_response(request)

        voting_time = VotingTime.objects.last()
        start = voting_time.start
        end = voting_time.end

        time = timezone.now()
        print(time)

        if time >= start and time <= end:
            return get_response(request)

        return blank(request)

    return middleware
