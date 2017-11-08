from django.contrib import admin
from .models import Question

# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Question group title', {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
        ]

admin.site.register(Question, QuestionAdmin)