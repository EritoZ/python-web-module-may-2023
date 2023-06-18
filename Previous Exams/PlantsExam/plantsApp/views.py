from django.shortcuts import render, redirect

from plantsApp.forms import EditPlantForm, CreatePlantForm, DeletePlantForm, CreateUserForm, EditUserForm
from plantsApp.models import Plant, UserProfile
from plantsApp.templatetags.profile_tags import search_profile


# Create your views here.

def find_plant(object_id):
    plant = Plant.objects.filter(id=object_id).get()

    return plant


def home(request):
    return render(request, 'common/home-page.html')


def profile_create(request):
    form = CreateUserForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('catalogue')

    context = {
        'form': form,
        'form_errors': form.errors
    }

    return render(request, 'profile/create-profile.html', context)


def plant_create(request):
    form = CreatePlantForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('catalogue')

    context = {
        'form': form,
        'form_errors': form.errors
    }

    return render(request, 'plant/create-plant.html', context)


def profile_delete(request):

    user: UserProfile = search_profile()

    if request.method == 'POST':
        user.delete()

        Plant.objects.all().delete()

        return redirect('home')

    return render(request, 'profile/delete-profile.html')


def profile_details(request):

    user: UserProfile = search_profile()

    plants_objects = Plant.objects.all()

    context = {
        'user': user,
        'plants_objects': plants_objects,
    }

    return render(request, 'profile/profile-details.html', context)


def profile_edit(request):

    user = search_profile()

    form = EditUserForm(request.POST or None, instance=user)

    if form.is_valid():
        form.save()
        return redirect('profile details')

    context = {
        'form': form,
        'form_errors': form.errors
    }

    return render(request, 'profile/edit-profile.html', context)


def catalogue(request):
    all_plants = Plant.objects.all()

    context = {
        'all_plants': all_plants
    }

    return render(request, 'common/catalogue.html', context)


def plant_details(request, plant_id):
    plant = find_plant(plant_id)

    context = {
        'plant': plant
    }

    return render(request, 'plant/plant-details.html', context)


def plant_edit(request, plant_id):
    plant = find_plant(plant_id)

    form = EditPlantForm(request.POST or None, instance=plant)

    if form.is_valid():
        form.save()
        return redirect('catalogue')

    context = {
        'form': form,
        'plant_id': plant_id,
    }

    return render(request, 'plant/edit-plant.html', context)


def plant_delete(request, plant_id):
    plant = find_plant(plant_id)

    if request.method == 'GET':
        form = DeletePlantForm(instance=plant)

    else:
        plant.delete()
        return redirect('catalogue')

    context = {
        'form': form,
        'plant_id': plant_id,
    }

    return render(request, 'plant/delete-plant.html', context)
