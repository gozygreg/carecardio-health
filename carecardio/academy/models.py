from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

PROFESSION_CHOICES = [
    ("Cardiac nurse", "Cardiac Nurse"),
    ("Cardiology Registra", "Cardiology Registra"),
    ("Cardiac Physiologist", "Cardiac Physiologist"),
    ("Radiographer", "Radiographer"),
    ("Student Nurse", "Student Nurse"),
    ("Medical Student", "Medical Student"),
    ("Student Physiologist", "Student Physiologist"),
    ("Student Radiographer", "Student Radiographer"),
]


class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = CloudinaryField('image', blank=True, null=True)

    def __str__(self):
        return self.title


class Module(models.Model):
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="modules")
    title = models.CharField(max_length=255)
    description = models.TextField()
    video = CloudinaryField(
        'video', resource_type='video', blank=True, null=True)
    video_width = models.PositiveIntegerField(default=640)
    video_height = models.PositiveIntegerField(default=360)
    pdf = CloudinaryField(
        'pdf', resource_type="image", blank=True, null=True)

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
    module = models.ForeignKey(
        Module, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255)
    profession = models.CharField(max_length=50, choices=PROFESSION_CHOICES)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.user.username} - {self.course.title}"
