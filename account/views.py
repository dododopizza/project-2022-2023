from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, ProfileEditForm, LoginForm, ProjectsEditForm
from . import models
from django.contrib.auth import authenticate, login, logout
from datetime import datetime

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            profile = models.Profile.objects.create(user=new_user, date_reg=int(datetime.today().strftime('%Y%m%d')))
            project = models.Project.objects.create(user=new_user)
            return redirect('login')
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})

def user_login(request):
    err = 0
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)

                    if get_object_or_404(models.Profile, pk=request.user.id).role == None:
                        return redirect('edit')
                    else:
                        return redirect('/account/profile/{}/'.format(request.user.id))
                else:
                    form = LoginForm()
                    err = 1
                    render(request, 'account/login.html', {'form': form,
                    'err': err,
                    })
            else:
                form = LoginForm()
                err = 1
                render(request, 'account/login.html', {'form': form,
                'err': err,
                })
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form,
    'err': err,
    })

@login_required
def edit_profile(request):
    err = 0
    try:
        id_user = request.user.id
    except:
        id_user = False
    if request.method == 'POST':
        profile = models.Profile.objects.get(user = request.user)
        profile_form = ProfileEditForm(instance=profile, data=request.POST, files=request.FILES)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('/account/profile/{}/'.format(id_user))
        else:
            err = 1
            profile = models.Profile.objects.get(user = request.user)
            profile_form = ProfileEditForm(request.POST, instance = profile)
            return render(request,
                      'account/edit.html',
                      {'profile_form': profile_form,
                      'err': err,
                      'id':id_user,
                      })
    else:
        profile = models.Profile.objects.get(user = request.user)
        profile_form = ProfileEditForm(instance=profile)
        return render(request,
                      'account/edit.html',
                      {'profile_form': profile_form,
                      'err': err,
                      'id':id_user,
                      })

def edit_projects(request):
    err = 0
    try:
        id_user = request.user.id
    except:
        id_user = False
    if request.method == 'POST':
        project = models.Project.objects.get(user=request.user)
        tr = request.POST.copy()
        tr['date'] = datetime.today().strftime('%d %B %Y')
        project_form = ProjectsEditForm(instance=project, data=tr)
        if project_form.is_valid():
            project_form.save()
            return redirect('/account/profile/{}/'.format(id_user))
        else:
            err = 1
            return render(RequestContext(request), 'account/editpr.html', {
            'pr_form': project_form,
            'err': err,
            'id':id_user,
            })
    project_form = ProjectsEditForm(instance=request.user)
    return render(request, 'account/editpr.html', {
    'pr_form': project_form,
    'err': err,
    'id':id_user,
    })

def profile(request, pk):
    # User = models.Profile.objects.get(user=request.user)
    # project = models.Project.objects.get(user=request.user)
    User = get_object_or_404(models.Profile, pk=pk)
    project = get_object_or_404(models.Project, pk=pk)
    User.email = User.email.split()
    try:
        id_user = request.user.id
    except:
        id_user = False
    return render(request, 'account/profile.html', {"profile": User,
    'project':project,
    'id':id_user,
    })

def Logout(request):
    logout(request)
    return redirect('/')

def project(request, pk):
    User = get_object_or_404(models.Profile, pk=pk)
    project = get_object_or_404(models.Project, pk=pk)
    try:
        id_user = request.user.id
    except:
        id_user = False
    return render(request, 'account/project.html', {"profile": User,
    'project':project,
    'id':id_user,
    })