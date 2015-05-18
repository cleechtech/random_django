from django.shortcuts import render
from .forms import UserProfileForm

def home(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UserProfileForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return render(request, 'name.html', {'form': form})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = UserProfileForm()

    return render(request, 'random_app/index.html', {'form': form})