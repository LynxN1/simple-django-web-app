from django import forms

from tasks.models import Task


class TaskForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Title', 'class': 'form-control'}), required=True, label='')

    class Meta:
        model = Task
        fields = ['title']
