from django import forms

class TaskForm(forms.Form):
    task = forms.CharField(max_length=100)
    description = forms.CharField(max_length=1000)
    due_date = forms.DateField()
    completed = forms.BooleanField()
