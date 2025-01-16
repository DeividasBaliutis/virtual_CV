import os
import random
from django.conf import settings
from django.http import FileResponse, Http404
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from cv.models import HomepageText, Hobby, PieChartData


def homepage(request):
    homepage_text = HomepageText.objects.first()
    return render(request, 'homepage.html', {'homepage_text': homepage_text})


def experience(request):
    pie_chart_data = PieChartData.objects.all().values_list('label', 'hours', 'color')

    labels = []
    hours = []
    colors = []

    for data in pie_chart_data:
        labels.append(data[0])
        hours.append(data[1])
        colors.append(data[2])

    return render(request, 'experience.html', {
        'labels': labels,
        'hours': hours,
        'colors': colors,
    })


def hobbies_view(request):
    hobbies = Hobby.objects.all()
    return render(request, 'hobbies.html', {'hobbys': hobbies})


def contacts(request):
    result = None
    user_choice = None
    computer_choice = None
    choices = ['rock', 'paper', 'scissors', ]

    if request.method == 'POST':
        user_choice = request.POST.get('user_choice')
        computer_choice = random.choice(choices)

        if user_choice == computer_choice:
            result = _('Draw!')
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
                (user_choice == 'scissors' and computer_choice == 'paper') or \
                (user_choice == 'paper' and computer_choice == 'rock'):
            result = _('You win! Contact number +37060631795 , email - DeividasBaliutis@gmail.com')
        else:
            result = _('Computer wins!')

    return render(request, 'contacts.html', {
        'user_choice': user_choice,
        'computer_choice': computer_choice,
        'result': result,
    })


def download_cv(request):
    file_path = os.path.join(settings.MEDIA_ROOT, 'CV.pdf')

    if not os.path.exists(file_path):
        raise Http404("CV failas nerastas.")

    try:
        return FileResponse(open(file_path, 'rb'), as_attachment=True, filename='CV.pdf')
    except Exception as klaida:
        raise Http404(f"Įvyko klaida bandant parsisiųsti failą: {klaida}")
