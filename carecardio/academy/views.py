from django.shortcuts import render, get_object_or_404
from .models import Course, Module, Quiz


def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    modules = Module.objects.filter(course=course)
    return render(request, 'academy/course_detail.html', {'course': course, 'modules': modules})


def module_detail(request, module_id):
    module = get_object_or_404(Module, id=module_id)
    # Assuming each module has only one quiz
    quiz = Quiz.objects.filter(module=module).first()
    return render(request, 'academy/module_detail.html', {'module': module, 'quiz': quiz})
