from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import NotificationForm
from .models import Notification
from .tasks import send_email


User = get_user_model()


def index(request):
    return render(request, 'index.html')


@login_required()
def notifications_list(request, username):
    author = get_object_or_404(User, username=username)
    if request.user != author:
        return redirect('notifications:notifications_list', username=request.user.username)
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
        send_email.delay(new_note.id)
        return redirect('notifications:index')
    return render(
        request,
        'new.html',
        {'form': form, 'header': header, 'action': action}
    )


@login_required()
def edit_notification(request, username, pk):
    header = 'Edit notification'
    action = 'Save'
    receiver = get_object_or_404(User, username=username)
    notification = get_object_or_404(Notification, pk=pk, receiver=receiver)
    if request.user != receiver:
        return redirect('notifications:notifications_list', username=username)
    form = NotificationForm(
        request.POST or None,
        files=request.FILES or None,
        instance=notification
    )
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(
                'notifications:notifications_list', username=username
            )

    context = {
        'form': form, 'notification': notification, 'header': header, 'action': action,
        'pk': pk, 'username': username,
    }
    return render(request, "new.html", context)


@login_required()
def delete_notification(request, username, pk):
    receiver = get_object_or_404(User, username=username)
    notification = get_object_or_404(Notification, pk=pk, receiver=receiver)
    if request.user != receiver:
        return redirect('notifications:notifications_list', username=username)
    notification.delete()
    return redirect('notifications:notifications_list', username=username)
