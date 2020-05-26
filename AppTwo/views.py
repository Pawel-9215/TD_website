from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User
from AppTwo.forms import NewUserForm
import json
import requests

def help(request):
    my_dick = {'help_script': "This is script for help page"}
    return render(request, "AppTwo/help.html", context=my_dick)

def index(request):
    #return HttpResponse("My Second App")
    commit_data = requests.get("https://api.github.com/repos/Pawel-9215/TerminalDungeon/commits/master").content
    commit_data_loaded=json.loads(commit_data)
    last_commit_date = commit_data_loaded["commit"]["author"]["date"][0:10]
    last_commit_msg = commit_data_loaded["commit"]["message"]

    form = NewUserForm()
    button_s = True
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            form = "Thank you for subscribing!"
            button_s = False
        else:
            print("ERR in form")

    index_dick = {'form':form, 'button':button_s, 'commit_date':last_commit_date, 'commit_msg':last_commit_msg} 

    return render(request, "AppTwo/index.html", index_dick)







def gallery(request):
    return render(request, "AppTwo/gallery.html")

def users(request):
    users_list = User.objects.order_by('last_name')
    user_dick = {'users': users_list}
    return render(request, "AppTwo/users.html", context=user_dick)


# Create your views here.
