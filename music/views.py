from django.shortcuts import render, redirect, get_object_or_404
from .models import Album
from music.forms import AlbumForm

def index(request): 
    albums = Album.objects.all()
    return render(request, 'music/index.html', {'albums': albums})

def album_detail(request, pk): 
    albums = Album.objects.get(pk=pk)
    return render(request, 'music/album_detail.html', {'album': albums})

def create_album(request): 
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            album = form.save()
        
            return redirect("home")

            
    else: 
        form = AlbumForm()
        # if user is visting a page with GET request, not submitting the form yet
    return render(request, 'music/create_album.html', {'form': form})

def album_edit(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == "POST":
        form = AlbumForm(request.POST, request.FILES, instance=album)
        if form.is_valid():
            album = form.save()
            album.user = request.user
            album.created_at = timezone.now()
            album.save()
            return redirect('album_detail', pk=album.pk)
    else:
        form = AlbumForm(instance=album)
    return render(request, 'music/album_edit.html', {'form': form})


def album_delete(request, pk):
    album = get_object_or_404(Album, pk=pk)
    # fetch the object related to passed id
    obj = get_object_or_404(Album, pk = pk)
    if request.method =="POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("/")
    return render(request, "music/album_delete.html", {})

