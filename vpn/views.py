# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect
from django.http import HttpResponse

from django.contrib import messages
from .models import ImageFeedback, VideoFeedback
from .forms  import ImageFeedbackForm, VideoFeedbackForm

# Create your views here.

def index(request):
    return render(request, "vpn/home.html", {})

def about(request):
    return render(request, "vpn/about.html", {})

def contact(request):
    return render(request, "vpn/contact.html", {})

# def feedback(request):
#     return render(request, "vpn/feedback.html", {})

def facilities(request):
    return render(request, "vpn/facilities.html", {})

def invitation(request):
    return render(request, "vpn/invitation.html", {})

def reach(request):
    return render(request, "vpn/reach.html", {})

def functionaries(request):
    return render(request, "vpn/functionaries.html", {})

def student_functionaries(request):
    return render(request, "vpn/student_functionaries.html", {})

def director(request):
    return render(request, "vpn/director.html", {})

def registrar(request):
    return render(request, "vpn/registrar.html", {})

def office(request):
    return render(request, "vpn/office.html", {})

def placement(request):
    return render(request, "vpn/placement.html", {})

def record(request):
    return render(request, "vpn/record.html", {})

def recruiters(request):
    return render(request, "vpn/recruiters.html", {})

def internship(request):
    return render(request, "vpn/internship.html", {})

def opportunities(request):
    return render(request, "vpn/opportunities.html", {})

def handler404(request, exception):
    return render(request, 'vpn/404.html', status=404)

def handler500(request):
    return render(request, 'vpn/500.html', status=500)




# def feedback_submit(request):
#     if request.method == 'POST':
#         form = FeedbackForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Your feedback has been submitted successfully!")
#             return redirect('feedback_page')  
#         else:
#             messages.error(request, "There was an error with your submission. Please check the form and try again.")
#     else:
#         form = FeedbackForm()

#     feedback_list = Feedback.objects.order_by('-created_at')
#     return render(request, 'vpn/feedback.html', {'form': form, 'feedback_list': feedback_list})


# def feedback_page(request):
#     form = FeedbackForm()
#     # all_feedbacks = Feedback.objects.all()
#     # print(all_feedbacks)
#     image_feedbacks = Feedback.objects.filter(image__isnull=False).order_by('-created_at')
#     video_feedbacks = Feedback.objects.filter(video__isnull=False).order_by('-created_at')
#     return render(request, 'vpn/feedback.html', {
#         'form': form,
#         'image_feedbacks': image_feedbacks,
#         'video_feedbacks': video_feedbacks,
#     })

def feedback_page(request):
    img_form = ImageFeedbackForm(prefix='img')
    vid_form = VideoFeedbackForm(prefix='vid')

    if request.method == 'POST':
        if 'img-submit' in request.POST:
            img_form = ImageFeedbackForm(request.POST, request.FILES, prefix='img')
            if img_form.is_valid():
                img_form.save()
                return redirect('feedback_page')
        elif 'vid-submit' in request.POST:
            vid_form = VideoFeedbackForm(request.POST, request.FILES, prefix='vid')
            if vid_form.is_valid():
                vid_form.save()
                return redirect('feedback_page')

    image_feedbacks = ImageFeedback.objects.order_by('-created_at')
    video_feedbacks = VideoFeedback.objects.order_by('-created_at')

    return render(request, 'vpn/feedback.html', {
        'img_form': img_form,
        'vid_form': vid_form,
        'image_feedbacks': image_feedbacks,
        'video_feedbacks': video_feedbacks,
    })