from asyncio import tasks
from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

# Line below isn't good because it will be shared among all app's session for different users 
# Then instead we can use Django Session as is in line 16 
#TASKS = list()

class NewTaskForm(forms.Form): 
    task = forms.CharField(label="New Task")
    priority = forms.IntegerField(label="Priority", min_value=1, max_value=10)

# Create your views here.
def index(request): 
    if "tasks" not in request.session: 
        request.session["tasks"] = list()
    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"] 
    })

def add(request): 
    # Check if teh form is valid and add the nw task | Server Side 
    if request.method == "POST": 
        form = NewTaskForm(request.POST)
        if form.is_valid(): 
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            # Use django to redirect the user to a specific page
            return HttpResponseRedirect(reverse("tasks:index"))
        # Else display the form with the possible error entry
        else: 
            return render(request, "tasks/add.html", {
                "form": form
            })

    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })