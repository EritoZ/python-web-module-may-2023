from django import forms

from plantsApp.models import Plant, UserProfile


class BaseUserForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'


class CreateUserForm(BaseUserForm, forms.ModelForm):
    pass


class EditUserForm(BaseUserForm, forms.ModelForm):
    pass


class BasePlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = '__all__'


class CreatePlantForm(BasePlantForm, forms.ModelForm):
    pass


class EditPlantForm(BasePlantForm, forms.ModelForm):
    pass


class DeletePlantForm(BasePlantForm, forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.disable_fields()

    def disable_fields(self):
        for name in self.fields:
            self.fields[name].widget.attrs['disabled'] = True
