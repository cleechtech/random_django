# django-forms

# This is part 3 of our Django Tutorials

## Objective

Students will begin to work with several native components of Django

### Form Section

* Forms

* Formsets

* Widgets

* Admin Forms

## Let's Get Started

# 1) Create a new Django Project and App

* Name anything you like
* Use git/github (create your own repo)
* Use Virtualenv
* Create a url path and view to display an index.html template

# 2) Create Models (we will integrate a user profile model)

```
from django.db import models
from django.contrib.auth.models import User
import datetime

class Hobby(models.Model):
    name = models.CharField(max_length=128)

class UserProfile(models.Model):
    user = models.OneToOneField(User)

    # The additional attributes will include.
    birthdate = models.DateField(blank=True)

    HAIR_COLOR_CHOICES = (
        ('BLACK', 'Black'),
        ('BROWN', 'Brown'),
        ('RED', 'Red'),
        ('BLONDE', 'Blonde'),
        ('SALTNPEPPER', 'Salt N Peppa'),
        ('GREEN', 'Green'),
    )

    hair_color = models.CharField(max_length=128,
                                      choices=HAIR_COLOR_CHOICES,
                                      blank=True)

    favorite_hobby = models.OneToOneField(Hobby)

    created = models.DateTimeField(default=datetime.datetime.now)

    def __unicode__(self):
        return self.user.username
```

# 3) Create Some Model Forms

Which file should we use?
What else do we need to include?

```
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['hair_color', 'birthdate', 'favorite_hobby', 'created'] # only show these fields
        # fields = '__all__' # default behavior
        # exclude = ['birthdate', 'favorite_hobby',] # don't show these fields
```

# 4) Use them into a view and template

Here is an example for a form called NameForm.  I'd like YOU to write the code for UserProfileForm 

```
def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return render(request, 'name.html', {'form': form})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})
```

# 5) Display your form in a template

```
<form method="post" action="">
    {{ form.as_p }}
</form>
```

# 6) Let's See our Data in the Admin Section

How do we add a model into the admin area?  Please do this yourself.  Then we will review the admin area as a class.

# 6) Add some new model fields

Use Local Flavor (Find in the docs)

```
phone =
city = 
state = 
zipcode = 
```