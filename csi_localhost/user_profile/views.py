from django.contrib.auth import logout as log_me_out
from django.shortcuts import render, redirect

from .forms import ProfileForm
from .models import Profile


# Create your views here.
def profile_view(request):
    user = request.user
    if user.is_authenticated:
        if request.method == "POST":
            form = ProfileForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                form.user = request.user
                form.save()
                return render(request, 'profile/start.html')
        elif request.method == "GET":
            try:
                profile = user.profile
                return render(request, 'profile/start.html')
            except Profile.DoesNotExist:
                form = ProfileForm(initial={'nick_name': user.username})
                return render(request, 'profile/profile.html', {'form': form})
    else:
        return redirect('home')


def leader_view(request):
    profiles = Profile.objects.all().order_by('-marks')
    if request.user.is_authenticated:
        text = "Let's Start"
        try:
            profile = request.user.profile
            if profile:
                if profile.current_question:
                    text = "Let's Continue"
        except Profile.DoesNotExist:
            pass
    return render(request, 'profile/lead.html', {"profiles": profiles, "text": text})


def logout(request):
    log_me_out(request)
    return redirect('home')
