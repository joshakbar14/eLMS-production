from django.contrib import admin

# Register your models here.
from .models import Student, Teacher, Course, Department, Assignment, Announcement, Material

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(Department)
admin.site.register(Assignment)
admin.site.register(Announcement)
# admin.site.register(Material)
