from django import forms

class ReminderForm(forms.Form):
    name = forms.CharField(max_length=150)
    time = forms.DateTimeField()
    phone_number = forms.CharField(max_length=15)
    message = forms.CharField(max_length=150)
