from django.shortcuts import render, redirect

from CarCollectionApp.forms import CreateProfileForm, CreateCarForm, DetailsCarForm, DeleteCarForm, EditProfileForm
from CarCollectionApp.models import ProfileModel, CarModel
from CarCollectionApp.templatetags.profile_tags import search_profile


# Create your views here.

def get_car(id):
    return CarModel.objects.filter(id=id).get()


def index(request):
    return render(request, 'common/index.html')


def catalogue(request):
    all_cars = CarModel.objects.all()

    context = {
        'all_cars': all_cars
    }

    return render(request, 'common/catalogue.html', context=context)


def profile_create(request):
    form = CreateProfileForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()

        return redirect('catalogue')

    context = {
        'form': form,
        'field_errors': form.errors,
    }

    return render(request, 'profile/profile-create.html', context=context)


def profile_details(request):
    profile: ProfileModel = search_profile()

    car_prices = list(CarModel.objects.values_list('price'))
    
    price_cars = sum(price[0] for price in car_prices)

    context = {
        'profile': profile,
        'total_price': price_cars
    }

    return render(request, 'profile/profile-details.html', context)


def profile_delete(request):
    profile: ProfileModel = search_profile()

    if request.method == 'POST':
        profile.delete()
        CarModel.objects.all().delete()

        return redirect('index')

    return render(request, 'profile/profile-delete.html')


def profile_edit(request):
    profile: ProfileModel = search_profile()

    form = EditProfileForm(request.POST or None, instance=profile)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('catalogue')

    context = {
        'form': form,
        'field_errors': form.errors,
    }

    return render(request, 'profile/profile-edit.html', context)


def car_create(request):
    form = CreateCarForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()

        return redirect('profile details')

    context = {
        'form': form,
        'field_errors': form.errors,
    }

    return render(request, 'car/car-create.html', context=context)


def car_details(request, car_id):
    car = CarModel.objects.filter(id=car_id).get()

    context = {
        'car': car
    }

    return render(request, 'car/car-details.html', context=context)


def car_edit(request, car_id):
    car = get_car(car_id)

    form = CreateCarForm(request.POST or None, request.FILES or None, instance=car)

    if request.method == 'POST' and form.is_valid():
        form.save()

        return redirect('catalogue')

    context = {
        'form': form,
        'field_errors': form.errors,
        'car': car
    }

    return render(request, 'car/car-edit.html', context)


def car_delete(request, car_id):
    car = get_car(car_id)

    form = DeleteCarForm(request.POST or None, instance=car)

    if request.method == 'POST':
        car.delete()
        return redirect('catalogue')

    context = {
        'form': form,
        'car': car
    }

    return render(request, 'car/car-delete.html', context)
