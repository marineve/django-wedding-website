from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from guests.save_the_date import SAVE_THE_DATE_CONTEXT_MAP


@login_required
def home(request):
    return render(request, 'home.html', context={
        'save_the_dates': SAVE_THE_DATE_CONTEXT_MAP,
        'support_email': settings.DEFAULT_WEDDING_REPLY_EMAIL,
    })
