from django.shortcuts import render
from django.core.serializers import serialize
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.conf import settings
import json, ast

from .models import Hospbeds
# Create your views here.

def HealthDash(request):
    # context = {'site_url':settings.MY_SITE_URL}
    # return render(request,"health_dash/health.html",context)
    obj=Hospbeds.objects.all()
    # # raw = Hospbeds.objects.raw('SELECT * FROM "HospBeds"')
    # ser_test=serialize('geojson',objk)
    # context = {'Hospbeds':ser_test}  # send data to front end
    # return render(request,"health_dash/health.html",context)
    ser_test = serialize('geojson',obj,)
    #context = {'image_loc':ser_test},fields=('geom',)
    

    hospbeds = json.loads(ser_test)
    hospbeds = json.dumps(hospbeds)
    return render(request,"health_dash/health.html",{
                          'hospbeds': hospbeds
                         })

def UrbanHealth(request):
    return render(request,"health_dash/town_health.html")
 
def trialDash(request):
    return render(request,"health_dash/trial.html")

def contribute(request):
    return render(request,"health_dash/contribute.html")

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/contribute')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "health_dash/login.html",
                    context={"form":form})


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("/")

