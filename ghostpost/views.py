from django.shortcuts import render, HttpResponseRedirect, reverse
from django.utils.timezone import now
from ghostpost.models import GhostPoster
from ghostpost.forms import RoastorBoastAddForm


def index(request):
    html = "index.html"
    post = GhostPoster.objects.all().order_by('-submission_time')
    return render(request, html, {'data': post})


def ghostpostaddview(request):
    html = "post_add_form.html"
    if request.method == "POST":
        form = RoastorBoastAddForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            GhostPoster.objects.create(
                is_boast=data['is_boast'],
                post=data['post'],
                submission_time=now()
            )
        return HttpResponseRedirect(reverse('/'))
    form = RoastorBoastAddForm(request.POST)
    return render(request, html, {'form': form})


def up_votes(request, id):
    try:
        post = GhostPoster.objects.get(id=id)
    except GhostPoster.DoesNotExist():
        return HttpResponseRedirect(reverse('/'))
    post.up_votes += 1
    post.total_votes += 1
    post.save()
    return HttpResponseRedirect(reverse('/'))


def down_votes(request, id):
    try:
        post = GhostPoster.objects.get(id=id)
    except GhostPoster.DoesNotExist():
        return HttpResponseRedirect(reverse('/'))
    post.down_votes += 1
    post.total_votes -= 1
    post.save()
    return HttpResponseRedirect(reverse('/'))


def sort_is_a_boast(request):
    html = 'index.html'
    posts = GhostPoster.objects.all().filter(
        is_boast=True).order_by('-submission_time')
    return render(request, html, {'data': posts})


def sort_is_a_roast(request):
    html = 'index.html'
    posts = GhostPoster.objects.all().filter(
        is_boast=False).order_by('-submission_time')
    return render(request, html, {'data': posts})


def sort_all_posts(request):
    posts = GhostPoster.objects.order_by('-total_votes')
    return render(request, 'index.html', {'data': posts})
