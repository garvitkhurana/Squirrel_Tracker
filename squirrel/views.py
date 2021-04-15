from django.shortcuts import render, redirect
from django.http import HttpResponse 

from .models import Sighting
from .forms import SightingForm


def homepage(request):
    return render(request, 'squirrel/homepage.html')

                                                                                                 
def add_sighting(request):
    if request.method == "POST":
        form= SightingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings')
    else:
        form = SightingForm()
        context ={
                'form':form,
                }
    return render(request,'squirrel/add.html',context)


def edit_sighting(request,SQUIRREL_ID):
    squirrel= Sighting.objects.get(SQUIRREL_ID=SQUIRREL_ID)
    if request.method =='POST':
        form = SightingForm(request.POST, instance = squirrel)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings')
    else:
        form = SightingForm(instance=squirrel)
        context ={
            'form':form,
                }
    return render(request, 'squirrel/update.html', context)

def map(request):
    sightings= Sighting.objects.all()[:100]
    context ={
            'sightings':sightings,
            }
    return render(request, 'squirrel/map.html', context)

def sighting(request):
    squirrels = Sighting.objects.all()
    context = {
            'sighting': squirrels,
        }
    return render(request, 'squirrel/sightings.html',context)

def get_statistics(request):
    AM = 0
    PM = 0
    G = 0
    C = 0
    B = 0
    for m in Sighting.objects.all():
        if m.SHIFT == 'AM':
            AM += 1
        if m.SHIFT == 'PM':
            PM += 1
        if m.FUR_COLOR == 'Gray':
            G += 1
        if m.FUR_COLOR == 'Cinnamon':
            C += 1
        if m.FUR_COLOR == 'Black':
            B += 1
    context = {
	'AM':AM,
	'PM':PM,
	'G':G,
	'C':C,
	'B':B,
	}
    return render(request, 'squirrel/statistics.html', context)
