from django import forms

from CarCollectionApp.models import ProfileModel, CarModel


class BaseProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = '__all__'
        widgets = {
            'password': forms.PasswordInput(render_value=True),
        }


class CreateProfileForm(BaseProfileForm):
    pass


class EditProfileForm(BaseProfileForm):
    pass


class BaseCarForm(forms.ModelForm):
    class Meta:
        model = CarModel
        fields = '__all__'


class DetailsCarForm(BaseCarForm):
    pass


class CreateCarForm(BaseCarForm):
    pass


class DeleteCarForm(BaseCarForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.disable_fields()

    def disable_fields(self):
        for field in self.fields:
            self.fields[field].widget.attrs['disabled'] = True
