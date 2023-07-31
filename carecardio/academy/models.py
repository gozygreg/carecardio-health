from django.db import models
from django.contrib.auth.models import User

PROFESSION_CHOICES = [
    ('Cardiac nurse', 'Cardiac Nurse'),
    ('Cardiology Registra', 'Cardiology Registra'),
    ('Cardiac Physiologist', 'Cardiac Physiologist'),
    ('Radiographer', 'Radiographer'),
    ('Student Nurse', 'Student Nurse'),
    ('Medical Student', 'Medical Student'),
    ('Student Physiologist', 'Student Physiologist'),
    ('Student Radiographer', 'Student Radiographer'),
]


class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title


class Module(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    video = models.URLField()

    def __str__(self):
        return self.title


class Quiz(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.content


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.content


class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    profession = models.CharField(max_length=50, choices=PROFESSION_CHOICES)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.user.username} - {self.course.title}"
