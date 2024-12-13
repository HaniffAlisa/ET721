from django.shortcuts import render, get_object_or_404, redirect
from .models import FeedbackPost
from .forms import FeedbackPostForm

def post_list(request):
    posts = FeedbackPost.objects.all()
    return render(request, 'feedback/post_list.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(FeedbackPost, id=post_id)
    return render(request, 'feedback/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = FeedbackPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_detail', post_id=post.id)  # Update this line
    else:
        form = FeedbackPostForm()
    return render(request, 'feedback/post_edit.html', {'form': form})

def edit_feedback(request, feedback_id):
    feedback = get_object_or_404(FeedbackPost, id=feedback_id)
    if request.method == 'POST':
        form = FeedbackPostForm(request.POST, instance=feedback)
        if form.is_valid():
            form.save()
            return redirect('post_detail', post_id=feedback.id)
    else:
        form = FeedbackPostForm(instance=feedback)
    return render(request, 'feedback/post_edit.html', {'form': form, 'feedback': feedback})