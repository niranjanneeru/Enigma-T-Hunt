from django.http import HttpResponse
from django.shortcuts import render

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
        else:
            try:
                profile = user.profile
                return render(request, 'profile/start.html')
            except Profile.DoesNotExist:
                form = ProfileForm(initial={'nick_name': user.username})
                return render(request, 'profile/profile.html', {'form': form})
