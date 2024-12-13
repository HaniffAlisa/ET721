from django.shortcuts import render, get_object_or_404, redirect
from .models import Item, Feedback
from .forms import FeedbackForm
from django.db.models import Avg

def homepage(request):
    return render(request, 'feedback/homepage.html')

def item_detail(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    feedbacks = Feedback.objects.filter(item=item)
    average_rating = feedbacks.aggregate(Avg('rating'))['rating__avg']
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.item = item
            feedback.save()
            return redirect('item_detail', item_id=item.id)
    else:
        form = FeedbackForm()
    return render(request, 'feedback/item_detail.html', {
        'item': item,
        'feedbacks': feedbacks,
        'average_rating': average_rating,
        'form': form
    })

def feedback_list(request):
    items = Item.objects.all()
    return render(request, 'feedback/feedback_list.html', {'items': items})