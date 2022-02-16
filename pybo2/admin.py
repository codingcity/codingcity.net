from django.contrib import admin
from .models import Question2

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']


admin.site.register(Question2, QuestionAdmin)