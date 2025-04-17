# admin.py
from django.contrib import admin
from .models import ImageFeedback, VideoFeedback
from .forms import ImageFeedbackForm, VideoFeedbackForm
# from .forms import FeedbackForm

class ImageFeedbackAdmin(admin.ModelAdmin):
    form = ImageFeedbackForm
    list_display = ('company_name', 'person_name', 'created_at')
    search_fields = ('company_name', 'person_name')

class VideoFeedbackAdmin(admin.ModelAdmin):
    form = VideoFeedbackForm
    list_display = ('company_name', 'person_name', 'created_at')
    search_fields = ('company_name', 'person_name')

admin.site.register(ImageFeedback, ImageFeedbackAdmin)
admin.site.register(VideoFeedback, VideoFeedbackAdmin)
