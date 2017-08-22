from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from apps.common.utils import get_list_display
from .models import Block, Lesson, Topic

# Headers
admin.site.site_header = _('Admin panel')
admin.site.site_title = ''
admin.site.index_title = ''


# Models
class TopicAdmin(admin.ModelAdmin):
    list_display = get_list_display(Topic)


admin.site.register(Topic, TopicAdmin)


class LessonAdmin(admin.ModelAdmin):
    list_display = get_list_display(Lesson)


admin.site.register(Lesson, LessonAdmin)


class BookAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Block
        exclude = ()


class BlockAdmin(admin.ModelAdmin):
    list_display = get_list_display(Block)
    form = BookAdminForm


admin.site.register(Block, BlockAdmin)
