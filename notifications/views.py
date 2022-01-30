from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import NotificationForm
from .models import Notification


User = get_user_model()


def index(request):
    return render(request, 'index.html')


def notifications_list(request, username):
    author = get_object_or_404(User, username=username)
    notifications = author.notifications.all()
    notify_amt = notifications.count()
    context = {
        'author': author,
        'notifications': notifications,
        'notify_amt': notify_amt,
    }
    return render(request, 'notifications_list.html', context)


@login_required()
def new_notification(request):
    header = 'Add Notification'
    action = 'Add'
    form = NotificationForm(request.POST or None)
    if form.is_valid():
        new_note = form.save(commit=False)
        new_note.receiver = request.user
        new_note.save()
        return redirect('notifications:index')
    return render(
        request,
        'new.html',
        {'form': form, 'header': header, 'action': action}
    )
