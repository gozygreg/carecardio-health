from django.shortcuts import render, get_object_or_404, redirect
from .forms import EnrollmentForm
from .models import Course, Module, Quiz, Enrollment
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# View for listing all courses
def course_list(request):
    courses = Course.objects.all()
    return render(request, "academy/course_list.html", {"courses": courses})

# View for displaying course details
def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    modules = Module.objects.filter(course=course)
    return render(request, "academy/course_detail.html", {"course": course, "modules": modules})

# View for displaying module details
@login_required
def module_detail(request, module_id):
    module = get_object_or_404(Module, id=module_id)
    # Assuming each module has only one quiz
    quiz = Quiz.objects.filter(module=module).first()
    enrolled_course_ids = request.user.enrollment_set.values_list('course__id', flat=True)

    # Check if the user is enrolled in the course containing this module
    if module.course_id in enrolled_course_ids:
        return render(request, "academy/module_detail.html", {"module": module, "quiz": quiz})
    else:
        # Redirect the user to enroll in the course if not enrolled
        return redirect("enroll_course", course_id=module.course.pk)

# View for enrolling in a course and granting access to all modules in that course
@login_required
def enroll_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    
    # Check if the user is already enrolled
    enrollment, created = Enrollment.objects.get_or_create(user=request.user, course=course)

    if not created:
        form = EnrollmentForm(request.POST or None, instance=enrollment, user=request.user)
    else:
        form = EnrollmentForm(request.POST or None, user=request.user)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully enrolled in this course.')
            return redirect("course_detail", course_id=course_id)
        else:
            messages.error(request, 'There was an error processing your enrollment.')

    return render(request, "academy/enroll_course.html", {"form": form, "course": course})
