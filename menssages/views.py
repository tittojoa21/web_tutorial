from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Message
from django.contrib.auth.models import User

@login_required
def message_create_view(request):
    if request.method == 'POST':
        recipient = get_object_or_404(User, username=request.POST['recipient'])
        message = Message(sender=request.user, recipient=recipient, subject=request.POST['subject'], body=request.POST['body'])
        message.save()
    return render(request, 'messages/create.html')

@login_required
def message_list_view(request):
    messages = Message.objects.filter(recipient=request.user)
    return render(request, 'messages/list.html', {'messages': messages})
