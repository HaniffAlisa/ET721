from django.shortcuts import redirect, render, get_object_or_404
from .models import Item, Feedback
from .forms import FeedbackForm
from django.db.models import Avg
from django.http import HttpResponse


def home(request):
    return HttpResponse("Welcome to the Feedback System!")

def item_detail(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    feedbacks = Feedback.objects.filter(item=item)
    average_rating = feedbacks.aggregate(Avg('rating'))['rating__avg']
    form = FeedbackForm(request.POST or None)
    if form.is_valid():
        feedback = form.save(commit=False)
        feedback.item = item
        feedback.save()
        form = FeedbackForm()  # Reset the form after successful submission
    return render(request, 'feedback/item_detail.html', {
        'item': item,
        'feedbacks': feedbacks,
        'average_rating': average_rating,
        'form': form,
    })

def submit_feedback(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.item = item
            feedback.save()
            return redirect('item_detail', item_id=item.id)
    else:
        form = FeedbackForm()
    return render(request, 'submit_feedback.html', {'form': form, 'item': item})