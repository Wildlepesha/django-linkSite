from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# from .models import Profile


class UserRegForm(UserCreationForm):
    email = forms.EmailField(
        label='Введите Email',
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Введите Email'})
    )
    username = forms.CharField(
        label='Введите логин',
        required=True,
        help_text='Обязательное поле. Не более 150 символов. Только буквы, цифры и симмволы @/ . / + / - / _ .',
        widget=forms.TextInput(attrs={'placeholder': 'Введите имя'})
    )
    password1 = forms.CharField(
        label='Введите пароль',
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'pas-inp', 'placeholder': 'Введите пароль'})
    )


    class Meta:
        model = User
        fields = ['username', 'email', 'password1']


    def __init__(self, *args, **kwargs):
        super(UserRegForm, self).__init__(*args, **kwargs)
        del self.fields['password2']
        self.fields['password1'].help_text = '<ul><li>Ваш пароль не должен совпадать с вашим именем или другой' \
                                             ' персональной информацией или быть слишком похожим на нее' \
                                             '<li>Ваш пароль должен содержать как минимум 8 символов' \
                                             '<li>Ваш пароль не может быть одним из широко распространенных паролей' \
                                             '<li>Ваш пароль не может состоять только из цифр' \
                                             '</ul>'


class updateUserForm(forms.ModelForm):
    email = forms.EmailField(
        label='Email:',
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Введите Email'})
    )
    username = forms.CharField(
        label='Имя пользователя:',
        required=True,
        help_text='Обязательное поле. Не более 150 символов. Только буквы, цифры и симмволы @/ . / + / - / _ .',
        widget=forms.TextInput(attrs={'placeholder': 'Введите имя'})
    )

    class Meta:
        model = User
        fields = ['username','email']



