from django import forms
from .models import TaskModel
from categories.models import Category

class TaskForm(forms.ModelForm):
    category = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = TaskModel
        fields = '__all__'
        widgets = {
            'task_assign_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }