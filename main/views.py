from django.shortcuts import render, redirect
from account.models import Profile
from datetime import datetime

# Create your views here.

def index(request):
    profiles = Profile.objects.all()
    form = []
    if profiles:
        for elem in profiles:
            if elem.role != None:
                form += elem.role,
        form = set(form)
    res = reversed(Profile.objects.filter(date_reg=int(datetime.today().strftime('%Y%m%d'))))
    try:
        id_user = request.user.id
    except:
        id_user = False
    return render(request, "main/index.html", {
        'form' : form,
        'id':id_user,
        'res':res,
    })

def search(request):
    res = 0
    try:
        id_user = request.user.id
    except:
        id_user = False
    profiles = Profile.objects.all()
    form = []
    if profiles:
        for elem in profiles:
            form += elem.role,
        form = set(form)
    if request.method == "POST":
        res = Profile.objects.filter(role=request.POST['req'])
        return render(request, 'main/search.html',{
            'form': form,
            'res': res,
            'id':id_user,
        })
    return render(request, 'main/search.html', {
        'form': form,
        'res': res,
        'id':id_user,
    })
