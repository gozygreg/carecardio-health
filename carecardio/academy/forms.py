from django import forms
from .models import Enrollment

class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['name', 'profession', 'email', 'phone']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Pop the 'user' argument from kwargs
        super().__init__(*args, **kwargs)

        if user:
            self.user = user  # Store 'user' as an instance variable

            user_enrollment = Enrollment.objects.filter(user=self.user).first()
            if user_enrollment:
                self.fields['name'].initial = user_enrollment.name
                self.fields['profession'].initial = user_enrollment.profession
                self.fields['email'].initial = user_enrollment.email
                self.fields['phone'].initial = user_enrollment.phone
