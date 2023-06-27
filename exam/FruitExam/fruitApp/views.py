from django.shortcuts import render, redirect

from fruitApp.forms import CreateProfileForm, CreateFruitForm, DeleteFruitForm, EditProfileForm
from fruitApp.models import FruitModel
from fruitApp.templatetags import custom_tags


# Create your views here.
def index(request):
    return render(request, 'common/index.html')


def dashboard(request):
    all_fruits = FruitModel.objects.all()

    context = {
        'all_fruits': all_fruits
    }

    return render(request, 'common/dashboard.html', context)


def profile_create(request):
    form = CreateProfileForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('dashboard')

    context = {
        'form': form,
        'errors': form.errors
    }

    return render(request, 'profile/create-profile.html', context)


def profile_details(request):
    all_posts = FruitModel.objects.all()

    context = {
        'all_posts': all_posts.count()
    }

    return render(request, 'profile/details-profile.html', context)


def profile_edit(request):
    profile = custom_tags.find_profile()

    form = EditProfileForm(request.POST or None, instance=profile)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('profile details')

    context = {
        'form': form,
        'errors': form.errors
    }

    return render(request, 'profile/edit-profile.html', context)


def profile_delete(request):
    profile = custom_tags.find_profile()

    if request.method == 'POST':
        profile.delete()
        FruitModel.objects.all().delete()
        return redirect('index')

    return render(request, 'profile/delete-profile.html')


def fruit_create(request):
    form = CreateFruitForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('dashboard')

    context = {
        'form': form,
        'errors': form.errors
    }

    return render(request, 'fruit/create-fruit.html', context)


def fruit_details(request, fruit_id):
    fruit = FruitModel.objects.filter(id=fruit_id).get()

    context = {
        'fruit': fruit
    }

    return render(request, 'fruit/details-fruit.html', context)


def fruit_edit(request, fruit_id):
    fruit = FruitModel.objects.filter(id=fruit_id).get()

    form = CreateFruitForm(request.POST or None, instance=fruit)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('dashboard')

    context = {
        'form': form,
        'errors': form.errors,
        'fruit_id': fruit_id
    }

    return render(request, 'fruit/edit-fruit.html', context)


def fruit_delete(request, fruit_id):
    fruit = FruitModel.objects.filter(id=fruit_id).get()

    form = DeleteFruitForm(request.POST or None, instance=fruit)

    if request.method == 'POST':
        fruit.delete()
        return redirect('dashboard')

    context = {
        'form': form,
        'fruit_id': fruit_id
    }

    return render(request, 'fruit/delete-fruit.html', context)
