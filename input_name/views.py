from django.shortcuts import render
import json

from .models import Name
from .forms import NameForm
# Create your views here.

def index(request):

    if request.method == 'POST':
        form = NameForm(request.POST)

        if form.is_valid():
            json_form = json.dumps(list(form.data.items()))
            name = Name(
                    name=json_form
                )
            name.save()

    else:

        form = NameForm()

    return render(request, 'input/index.html', {'form': form})



def results(request):

    latest_name_list = Name.objects.all()
    context = {'latest_name_list': latest_name_list}
    return render(request, 'input/results.html', context)




