from django.shortcuts import render
from django.views import View
from .tasks import go_to_sleep


class TestCelery(View):
    def get(self, request):
        go_to_sleep.delay(6)
        return render(request, "polls/test_celery.html")
