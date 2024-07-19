from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import UserProfile
from .forms import UserProfileForm, UserForm
from access.models import Access

@login_required
def profile_view(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    userprofile = get_object_or_404(UserProfile, user=user)
    accesses = userprofile.access_set.all()  # assuming UserProfile has a relation to Access
    return render(request, 'userprofile/profile.html', {'userprofile': userprofile, 'accesses': accesses})

@login_required
def my_profile(request):
    userprofile = get_object_or_404(UserProfile, user=request.user)
    accesses = Access.objects.filter(user=request.user)
    return render(request, 'userprofile/my_profile.html', {'userprofile': userprofile, 'accesses': accesses})

@login_required
def edit_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    user_profile = get_object_or_404(UserProfile, user=user)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('user_list')
    else:
        user_form = UserForm(instance=user)
        profile_form = UserProfileForm(instance=user_profile)
    return render(request, 'userprofile/edit_user.html', {'user_form': user_form, 'profile_form': profile_form})


def user_list(request):
    users = User.objects.all()
    return render(request, 'userprofile/user_list.html', {'users': users})