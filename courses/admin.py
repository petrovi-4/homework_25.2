from django.contrib import admin

from courses.models import Lesson, Course


@admin.register(Lesson)
class LeesonAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'course', 'owner')
    search_fields = ('title', 'course', 'owner')


@admin.register(Course)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'owner')
    search_fields = ('title', 'owner')
