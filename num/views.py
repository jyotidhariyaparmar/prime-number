from django.shortcuts import render
from .models import Prime
from .forms import PrimeForm


def home(request):
    return render(request, "home.html")


def create_view(request):
    firstnumber = request.POST.get('Firstnumber')

    lastnumber = request.POST.get('Lastnumber')

    submitbutton = request.POST.get('Submit')

    for number in range(firstnumber, (lastnumber) + 1):
        if number > 1:
            for i in range(2, number):
                if (number % i) == 0:
                    break
            else:
                context = {'  firstnumber': firstnumber, 'lastnumber': lastnumber, 'submitbutton': submitbutton,
                           'number': number}

    return render(request, 'create_view.html', context)


# form = PrimeForm(request.POST or None)
# context = {}
#
# if form.is_valid():
#     for number in range(request.POST.get('fnum') and request.POST.get('lnum') + 1):
#         if number > 1:
#             for i in range(2, number):
#                 if (number % i) == 0:
#                     break
#             else:
#                 print(number)
#     form.save()
# context['form'] = form
# return render(request, "create_view.html", context)


def list_view(request):
    context = {}

    context['dataset'] = Prime.objects.all()
    return render(request, "list_view.html", context)
