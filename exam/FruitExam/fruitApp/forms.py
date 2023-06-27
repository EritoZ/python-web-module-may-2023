from django import forms

from fruitApp.models import ProfileModel, FruitModel


class BaseProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = '__all__'


class CreateProfileForm(BaseProfileForm):
    class Meta(BaseProfileForm.Meta):
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'First Name'
                }),

            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Last Name'
                }
            ),

            'email': forms.TextInput(
                attrs={
                    'placeholder': 'Email'
                }
            ),

            'password': forms.TextInput(
                attrs={
                    'placeholder': 'Password',
                    'class': 'form-control',
                }
            ),
        }


class EditProfileForm(BaseProfileForm):
    class Meta(BaseProfileForm.Meta):
        exclude = ('email', 'password')


class BaseFruitForm(forms.ModelForm):
    class Meta:
        model = FruitModel
        fields = '__all__'


class CreateFruitForm(BaseFruitForm):
    class Meta(BaseFruitForm.Meta):
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Fruit Name'
                }),

            'image_url': forms.TextInput(
                attrs={
                    'placeholder': 'Fruit Image URL'
                }
            ),

            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Fruit Description'
                }
            ),

            'nutrition': forms.Textarea(
                attrs={
                    'placeholder': 'Nutrition Info',
                }
            ),
        }


class EditFruitForm(CreateFruitForm):
    pass


class DeleteFruitForm(BaseFruitForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.disable_fields()

    def disable_fields(self):
        for field in self.fields:
            self.fields[field].widget.attrs['disabled'] = True
