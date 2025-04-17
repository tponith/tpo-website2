# vpn/forms.py
from django import forms
from .models import ImageFeedback, VideoFeedback

class ImageFeedbackForm(forms.ModelForm):
    class Meta:
        model  = ImageFeedback
        fields = ['company_name','person_name','feedback_text','image']

class VideoFeedbackForm(forms.ModelForm):
    class Meta:
        model  = VideoFeedback
        fields = ['company_name','person_name','feedback_text','video']
