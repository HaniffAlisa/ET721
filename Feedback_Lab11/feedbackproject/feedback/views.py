from django.shortcuts import render, get_object_or_404
from .models import Item, Feedback
from .forms import FeedbackForm
from django.http import HttpResponse

# Create your views here.

def homepage(request):
    form = FeedbackForm()

    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()  # Save feedback to the database
            return render(request, 'feedback/success.html')  # Optional success page

    return render(request, 'feedback/homepage.html', {'form': form})

def item_detail(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    feedbacks = item.feedbacks.all()
    form = FeedbackForm()

    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.item = item
            feedback.save()
            return render(request, 'feedback/success.html')  # Change this as needed

    return render(request, 'feedback/item_detail.html', {
        'item': item,
        'feedbacks': feedbacks,
        'form': form,
    })