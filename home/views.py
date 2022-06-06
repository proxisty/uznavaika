from django.shortcuts import render
from django.views.generic import ListView, View
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect

from .forms import FeedBackForm
from .models import Lesson, Teacher, Price

class HomeView(ListView):
    model = Lesson
    context_object_name = 'lesson_list'
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['teacher_list'] = Teacher.objects.all()
        context['price_list'] = Price.objects.all()
        return context
    # def get_queryset(self):
    #     return Lesson.objects.all()


class FeedBackView(View):
    def get(self, request, *args, **kwargs):
        form = FeedBackForm()
        return render(request, 'feedback.html', context={
            'form': form,
            'title': 'Написать мне'
        })

    def post(self, request, *args, **kwargs):
        form = FeedBackForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            from_email = form.cleaned_data['email']
            subject = form.cleaned_data['phone']
            message = form.cleaned_data['description']
            try:
                # send_mail(f'От {name} | {subject}', message, from_email, ['amromashov@gmail.com'])
                print(f'От {name} | {subject}', message, from_email, ['amromashov@gmail.com'])
                form.save()
            except BadHeaderError:
                return HttpResponse('Невалидный заголовок')
            return HttpResponseRedirect('success')
        return render(request, 'contact.html', context={
            'form': form,
        })


class SuccessView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'success.html', context={
            'title': 'Спасибо'
        })
