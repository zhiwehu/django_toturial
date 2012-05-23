# Create your views here.
from django.core.urlresolvers import reverse
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from models import Bookmark
from forms import BookmarkForm

def index(request):
    bookmarks = Bookmark.objects.all()
    return render_to_response('index.html',
            {
            'bookmarks': bookmarks,
            })

def create(request):
    if request.method == 'POST': # If the form has been submitted...
        form = BookmarkForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            bookmark = form.save()
            return HttpResponseRedirect(reverse('bookmark_list')) # Redirect after POST
    else:
        form = BookmarkForm() # An unbound form

    return render_to_response('create.html',
        RequestContext(request, {
            'form': form,
            }))


def update(request, bookmark_id):
    try:
        bookmark = Bookmark.objects.get(id=bookmark_id)
    except Bookmark.DoesNotExist:
        raise Http404

    if request.method == 'POST': # If the form has been submitted...
        form = BookmarkForm(request.POST, instance=bookmark)
        if form.is_valid(): # All validation rules pass
            bookmark = form.save()
            return HttpResponseRedirect(reverse('bookmark_list')) # Redirect after POST
    else:
        form = BookmarkForm(instance=bookmark)

    return render_to_response('update.html',
        RequestContext(request, {
            'form': form,
            }))


def delete(request, bookmark_id):
    try:
        bookmark = Bookmark.objects.get(id=bookmark_id)
        bookmark.delete()
    except Bookmark.DoesNotExist:
        raise Http404
    return index(request)

def show(request, bookmark_id):
    try:
        bookmark = Bookmark.objects.get(id=bookmark_id)
    except Bookmark.DoesNotExist:
        raise Http404
    return render_to_response('show.html',
            {
            'bookmark': bookmark,
            })

