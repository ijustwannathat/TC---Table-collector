from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Comment


class SignUpForm(forms.Form):
    username = forms.CharField(
        max_length=64,
        required=True,
        widget=forms.TextInput(attrs={
            "class": "form-control mt-2",
            "id": "inputUsername",
            "placeholder": "Username"
        })
    )

    password = forms.CharField(
        max_length=128,
        required=True,
        widget=forms.TextInput(attrs={
            "class": "form-control mt-2",
            "id": "inputPassword",
            "placeholder": "Password"
        })
    )

    confirm_password = forms.CharField(
        max_length=128,
        required=True,
        widget=forms.TextInput(attrs={
            "class": "form-control mt-2",
            "id": "ReInputPassword",
            "placeholder": "Confirm password"
        })
    )

    def clean(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError(
                "Passwords do not mach, try again."
            )

    def save(self):
        user = User.objects.create_user(
            username=self.cleaned_data["username"],
            password=self.cleaned_data["password"]
        )
        auth = authenticate(**self.cleaned_data)
        return auth


class SignInForm(forms.Form):
    username = forms.CharField(
        max_length=64,
        required=True,
        widget=forms.TextInput(attrs={
            "class": "form-control mt-2",
            "id": "inputUsername",
            "placeholder": "Username",
        })
    )
    password = forms.CharField(
        max_length=128,
        required=True,
        widget=forms.TextInput(attrs={
            "class": "form-control mt-2",
            "id": "inputPassword",
            "placeholder": "Password",
        })
    )


class FeedBackForm(forms.Form):
    name = forms.CharField(
        max_length=64,
        required=True,
        widget=forms.TextInput(attrs={
            "class": "form-control mt-2",
            "id": "name",
            "placeholder": "Your name",
        })
    )
    email = forms.CharField(
        max_length=128,
        required=True,
        widget=forms.TextInput(attrs={
            "class": "form-control mt-2",
            "id": "email",
            "placeholder": "Your email",
        })
    )
    subject = forms.CharField(
        max_length=200,
        required=True,
        widget=forms.TextInput(attrs={
            "class": "form-control mt-2",
            "id": "subject",
            "placeholder": "Subject"
        })
    )
    message = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control mt-2",
            "id": "message",
            "rows": 2,
            "placeholder": "Your message",
        })
    )


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3
            }),
        }