from django import forms

from myMusicApp.models import ProfileModel, AlbumModel


class BaseProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = '__all__'


class CreateProfileForm(BaseProfileForm):
    class Meta(BaseProfileForm.Meta):
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'placeholder': 'Username',
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'placeholder': 'Email',
                }
            ),
            'age': forms.TextInput(
                attrs={
                    'placeholder': 'Age',
                }
            ),
        }


class DeleteProfileForm(BaseProfileForm):
    pass


class BaseAlbumForm(forms.ModelForm):
    class Meta:
        model = AlbumModel
        fields = '__all__'


class CreateAlbumForm(BaseAlbumForm):
    class Meta(BaseAlbumForm.Meta):
        widgets = {
            'album_name': forms.TextInput(
                attrs={
                    'placeholder': 'Album Name',
                },
            ),
            'artist': forms.TextInput(
                attrs={
                    'placeholder': 'Artist'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Description',
                }
            ),
            'image_url': forms.TextInput(
                attrs={
                    'placeholder': 'Image Url'
                }
            ),
            'price': forms.TextInput(
                attrs={
                    'placeholder': 'Price'
                }
            ),
        }


class EditAlbumForm(BaseAlbumForm):
    pass


class DeleteAlbumForm(BaseAlbumForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.disable_fields()

    def disable_fields(self):
        for field in self.fields:
            self.fields[field].widget.attrs['readonly'] = True

        self.fields['genre'].widget.attrs['disabled'] = True
