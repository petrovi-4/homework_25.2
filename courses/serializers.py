from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from courses.models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    number_of_lessons = SerializerMethodField()
    lesson = LessonSerializer(many=True, read_only=True)

    def get_number_of_lessons(self, course):
        return Lesson.objects.filter(course=course).count()

    class Meta:
        model = Course
        fields = ('id', 'title', 'description', 'preview_image', 'number_of_lessons', 'owner', 'lesson',)

