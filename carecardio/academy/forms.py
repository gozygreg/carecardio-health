from django import forms
from .models import Enrollment


class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        # Add any specific fields you want to include in the form if needed
        fields = ['user', 'course']
