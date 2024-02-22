from django.contrib import admin

from .models import Question, Module

class QuestionInLine(admin.StackedInline):
    model = Question
    extra = 1

# Register your models here.
@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'num_questions']
    inlines = [QuestionInLine]

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['pk','question_text', 'module', 'correct']
    