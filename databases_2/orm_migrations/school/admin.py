from django.contrib import admin

from .models import Student, Teacher, School


# @admin.register(Student)
# class StudentAdmin(admin.ModelAdmin):
#     pass
#
#
# @admin.register(Teacher)
# class TeacherAdmin(admin.ModelAdmin):
#     pass

class SchoolInline(admin.TabularInline):
    model = School
    extra = 1


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    inlines = (SchoolInline,)


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    inlines = (SchoolInline,)