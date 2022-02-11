from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .forms import CreationForm, UserUpdateForm


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('notifications:index')
    template_name = 'users/signup.html'


@login_required()
def profile(request):
    header = 'User profile'
    action = 'Update'
    if request.method == 'POST':
        form = UserUpdateForm(
            request.POST,
            request.FILES,
            instance=request.user
        )
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('users:profile')
    form = UserUpdateForm(instance=request.user)
    context = {
        'form': form, 'header': header, 'action': action,
    }
    return render(request, 'users/profile.html', context)
