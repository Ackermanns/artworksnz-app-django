from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Artist, Artwork
from .forms import ArtworkForm, ArtistForm

# Create your views here.
def home(request):
    return render(request, 'artworksnzapp/home.html')

@login_required
def artists(request):
    artist_data = Artist.objects.all()
    return render(request, 'artworksnzapp/artists.html', {'artist_data':artist_data})

@login_required
def artistshow(request, artistkey):
    artist_data = Artist.objects.get(pk=artistkey)
    artwork_data = Artwork.objects.all()
    context = {'artistkey':int(artistkey), 'artist_data':artist_data, 'artwork_data':artwork_data}
    return render(request, 'artworksnzapp/artistshow.html', context)

@login_required
def artworks(request):
    artist_data = Artist.objects.all()
    artwork_data = Artwork.objects.all()
    return render(request, 'artworksnzapp/artworks.html', {'artist_data':artist_data, 'artwork_data':artwork_data})

@login_required
def artworkshow(request, artworkkey):
    artwork_data = Artwork.objects.get(pk=artworkkey)
    artist_id = artwork_data.artist_id.id
    artist_data = Artist.objects.get(pk=artist_id)
    return render(request, 'artworksnzapp/artworkshow.html', {'artworkkey':int(artworkkey), 'artist_data':artist_data, 'artwork_data':artwork_data})

@login_required
def addartwork(request, artistkey):
    artistkey = int(artistkey)
    artworkform = ArtworkForm()
    #When visiting the page
    if request.method == 'GET':
        artworkform = ArtworkForm()
        return render(request, 'artworksnzapp/addartwork.html', {'artistkey':artistkey, 'artworkform':artworkform})
    #When submiting the form
    if request.method == 'POST':
        #Form data
        artworkform = ArtworkForm(request.POST, request.FILES)
        if artworkform.is_valid():
            artworkform.save()
            return redirect("/artists/"+str(artistkey))
        else:
            artworkform = ArtworkForm()
            return redirect('addartwork/'+str(artistkey))
            
@login_required
def addartist(request):
    #When visiting the page
    if request.method == 'GET':
        artist_form = ArtistForm()
        return render(request, 'artworksnzapp/addartist.html', {'artist_form':artist_form})
    #When submiting the form
    if request.method == 'POST':
        upload = ArtistForm(request.POST)
        if upload.is_valid():
            upload.save()
        return redirect('/artists/')

@login_required
def delete_artist(request, artistkey):
    artistkey = int(artistkey)
    artistobj = Artist.objects.get(pk=artistkey)
    artistobj.delete()
    return redirect("/artists/")

@login_required
def delete_artwork(request, artworkkey):
    artworkkey = int(artworkkey)
    artworkobj = Artwork.objects.get(pk=artworkkey)
    artworkobj.delete()
    return redirect("/artworks/")

@login_required
def edit_artist(request, artistkey):
    artistkey = int(artistkey)
    upload = ArtistForm()
    if request.method == 'GET':
        artistobj = Artist.objects.get(pk=artistkey)
        return render(request, 'artworksnzapp/editartist.html', {'artistobj':artistobj})
    if request.method == 'POST':
        #Get the form values
        upload = ArtistForm(request.POST)
        if upload.is_valid():
            upload.save()
        #Apply update
        return redirect("/artists/"+str(artistkey))
        
def edit_artwork(request, artworkkey):
    artworkkey = int(artworkkey)
    artworkobj = Artwork.objects.get(pk=artworkkey)
    artworkform = ArtworkForm(request.POST or None, request.FILES or None, instance=artworkobj)
    if request.method == 'GET':
        return render(request, 'artworksnzapp/editartwork.html', {'artworkform':artworkform})
    if request.method == 'POST':
        #add/change the form values
        artworkform = ArtworkForm(request.POST or None, request.FILES or None, instance=artworkobj)
        if artworkform.is_valid():
            artworkform.save()
            return redirect("/artworks/"+str(artworkkey))
