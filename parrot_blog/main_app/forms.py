from django import forms
from .models import Post
from ckeditor.widgets import CKEditorWidget
from bootstrap_app.forms import set_form_control


class PostForm(forms.ModelForm):
    title = forms.CharField(label='Заголовок',
                            widget=forms.TextInput(attrs={'placeholder': 'Заголовок'}))
    subtitle = forms.CharField(label='Подзаголовок',
                               widget=forms.TextInput(attrs={'placeholder': 'Подзаголовок'}))
    text = forms.CharField(label='Текст',
        widget=CKEditorWidget(attrs={'placeholder': 'Текст (поддерживается html)'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        set_form_control(self.fields)
        # for field in self.fields.values():
        #     field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Post
        fields = ('title', 'image', 'subtitle', 'text', 'is_active')
