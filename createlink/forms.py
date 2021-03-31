from django import forms
from .models import Link


class LinkForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(LinkForm, self).__init__(*args, **kwargs)
        self.fields['long'].label = 'Длинная ссылка'
        self.fields['long'].help_text = 'Не более 250 символов'
        self.fields['short'].label = 'Короткая ссылка'

    class Meta:
        model = Link
        fields = ['long', 'short']