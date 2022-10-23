from django.shortcuts import render, redirect
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