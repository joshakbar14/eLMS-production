from django.db import models
from main.models import Student, Teacher, Course


class StudentDiscussion(models.Model):
    content = models.TextField(max_length=1600, null=False)
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name='discussions')
    sent_by = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name='discussions')
    sent_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-sent_at']

    def __str__(self):
        return self.content[:30]

    def time(self):
        return self.sent_at.strftime("%d-%b-%y, %I:%M %p")


class TeacherDiscussion(models.Model):
    content = models.TextField(max_length=1600, null=False)
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name='courseDiscussions')
    sent_by = models.ForeignKey(
        Teacher, on_delete=models.CASCADE, related_name='courseDiscussions')
    sent_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-sent_at']

    def __str__(self):
        return self.content[:30]

    def time(self):
        return self.sent_at.strftime("%d-%b-%y, %I:%M %p")
