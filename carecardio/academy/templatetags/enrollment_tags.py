from django import template
from academy.models import Enrollment  # Import the Enrollment model

register = template.Library()

@register.filter(name='has_enrollment')
def has_enrollment(user, course):
    # Check if the user is enrolled in the specified course
    return Enrollment.objects.filter(user=user, course=course).exists()