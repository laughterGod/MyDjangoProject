from django.contrib import admin

# Register your models here.

from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text']
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']
    fieldsets = [
        ('Date information', {'fields': ['pub_date']}),
        ('Question information', {'fields': ['question_text']}),
    ]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)