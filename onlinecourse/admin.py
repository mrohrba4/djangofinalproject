from django.contrib import admin
# <HINT> Import any new Models here
from .models import Course, Lesson, Instructor, Learner, Question, Choice

# <HINT> Register QuestionInline and ChoiceInline classes here
class ChoiceAdmin(admin.StackedInline):
    model = Choice
    list_display = ('name', 'pub_date')

class QuestionAdmin(admin.StackedInline):
    model = Question
    list_display = ('name', 'pub_date')

class LessonInline(admin.StackedInline):
    model = Lesson
    list_display = ('name', 'pub_date')
    extra = 5


# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']


class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']


# <HINT> Register Question and Choice models here

admin.site.register(Choice)
admin.site.register(Question)
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
