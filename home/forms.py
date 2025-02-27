from django import forms
from .models import Student

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'room_no', 'mis', 'phone', 'dob', 'year', 'branch']
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),  # Show date picker
        }
