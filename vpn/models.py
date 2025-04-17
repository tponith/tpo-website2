# from django.db import models
# from django.core.exceptions import ValidationError

# def validate_media(instance):
#     """
#     Ensures that either the image or video field is provided.
#     """
#     if not instance.image and not instance.video:
#         raise ValidationError("You must upload at least an image or a video.")

# class Feedback(models.Model):
#     company_name = models.CharField(max_length=255)
#     person_name = models.CharField(max_length=255)
#     feedback_text = models.TextField()
#     image = models.ImageField(upload_to='feedback_images/', blank=True, null=True)
#     video = models.FileField(upload_to='feedback_videos/', blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def clean(self):
#         # Calling the custom validation function
#         validate_media(self)

#     def __str__(self):
#         return f"{self.company_name} - {self.person_name}"

# vpn/models.py
from django.db import models

class ImageFeedback(models.Model):
    company_name  = models.CharField(max_length=255)
    person_name   = models.CharField(max_length=255)
    feedback_text = models.TextField()
    image         = models.ImageField(upload_to='feedback_images/')
    created_at    = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.company_name} (Image)"

class VideoFeedback(models.Model):
    company_name  = models.CharField(max_length=255)
    person_name   = models.CharField(max_length=255)
    feedback_text = models.TextField()
    video         = models.FileField(upload_to='feedback_videos/')
    created_at    = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.company_name} (Video)"
