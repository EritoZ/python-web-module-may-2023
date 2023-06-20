from django.shortcuts import render, redirect

from myMusicApp.forms import CreateProfileForm, CreateAlbumForm, EditAlbumForm, DeleteAlbumForm
from myMusicApp.models import AlbumModel
from myMusicApp.templatetags.custom_tags import find_profile


# Create your views here.

def index(request):
    if not find_profile():
        form = CreateProfileForm(request.POST or None)

        if request.method == 'POST' and form.is_valid():
            form.save()
            return redirect('index')

        context = {
            'form': form,
            'errors': form.errors,
        }

        return render(request, 'common/home-no-profile.html', context)

    all_albums = AlbumModel.objects.all()

    context = {
        'all_albums': all_albums
    }

    return render(request, 'common/home-with-profile.html', context)


def profile_details(request):
    all_albums = AlbumModel.objects.all()

    context = {
        'all_albums': all_albums
    }

    return render(request, 'profile/profile-details.html', context)


def profile_delete(request):

    if request.method == 'POST':
        find_profile().delete()
        AlbumModel.objects.all().delete()
        return redirect('index')

    return render(request, 'profile/profile-delete.html')


def album_details(request, id):
    album = AlbumModel.objects.filter(id=id).get()

    context = {
        'album': album
    }

    return render(request, 'album/album-details.html', context)


def album_add(request):
    form = CreateAlbumForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('index')

    context = {
        'form': form,
        'errors': form.errors
    }

    return render(request, 'album/add-album.html', context)


def album_edit(request, id):
    album = AlbumModel.objects.filter(id=id).get()

    form = EditAlbumForm(request.POST or None, instance=album)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('index')

    context = {
        'form': form,
        'errors': form.errors,
        'album_id': id
    }

    return render(request, 'album/edit-album.html', context)


def album_delete(request, id):
    album = AlbumModel.objects.filter(id=id).get()

    form = DeleteAlbumForm(request.POST or None, instance=album)

    if request.method == 'POST':
        album.delete()
        return redirect('index')

    context = {
        'form': form,
        'album_id': id
    }

    return render(request, 'album/delete-album.html', context)
