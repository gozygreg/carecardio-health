from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import EnrollmentForm
from .models import Course, Module, Quiz


def course_list(request):
    courses = Course.objects.all()
    return render(request, 'academy/course_list.html', {'courses': courses, 'course': Course()})


def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    modules = Module.objects.filter(course=course)
    return render(request, 'academy/course_detail.html', {'course': course, 'modules': modules})


def is_user_enrolled(view_func):
    @login_required
    def _wrapped_view(request, module_id, *args, **kwargs):
        module = get_object_or_404(Module, id=module_id)
        enrolled_modules = request.user.enrollment_set.values_list(
            'course__module', flat=True)
        if module in enrolled_modules:
            return view_func(request, module_id, *args, **kwargs)
        else:
            return redirect('enroll_course', course_id=module.course.pk)

    return _wrapped_view


@login_required
def module_detail(request, module_id):
    module = get_object_or_404(Module, id=module_id)
    # Assuming each module has only one quiz
    quiz = Quiz.objects.filter(module=module).first()
    return render(request, 'academy/module_detail.html', {'module': module, 'quiz': quiz})


# Apply the custom decorator to the module_detail view
module_detail = is_user_enrolled(module_detail)


@login_required
def enroll_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            enrollment = form.save(commit=False)
            enrollment.user = request.user
            enrollment.course = course
            enrollment.save()
            return redirect('course_detail', course_id=course_id)
    else:
        form = EnrollmentForm()

    return render(request, 'academy/enroll_course.html', {'form': form, 'course': course})
