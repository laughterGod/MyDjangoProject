from django.contrib import admin

# Register your models here.

from .models import *
from .views import ks3_storage_submit, eip_submit


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


@admin.register(Question)
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


@admin.register(KS3Models)
class KS3ModelsAdmin(admin.ModelAdmin):
    def changelist_view(self, request, extra_content=None):
        return ks3_storage_submit(request, type(self).__name__)


@admin.register(KS3ArchiveModels)
class KS3ArchiveModelsAdmin(admin.ModelAdmin):
    def changelist_view(self, request, extra_content=None):
        return ks3_storage_submit(request, type(self).__name__)


@admin.register(EIPDayTransferModels)
class EIPDayTransferModelsAdmin(admin.ModelAdmin):
    def changelist_view(self, request, extra_content=None):
        return eip_submit(request, type(self).__name__)


@admin.register(BWSDayTransferModels)
class BWSDayTransferModelsAdmin(admin.ModelAdmin):
    def changelist_view(self, request, extra_content=None):
        return eip_submit(request, type(self).__name__)


admin.site.site_url = None


# admin.site.register(Question, QuestionAdmin)
# admin.site.register(KS3Models, KS3ModelsAdmin)
