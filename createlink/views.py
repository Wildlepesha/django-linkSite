from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Link
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import LinkForm

def home(request):
    return render(request, 'user/home.html', {'title':'Главная'})
class ShowLinks(ListView):
    model = Link
    template_name = 'user/av.html'
    context_object_name = 'post'
    paginate_by = 15

    def get_queryset(self):
        return Link.objects.filter(autor=self.request.user)

    def get_context_data(self, **kwargs):
        ctx = super(ShowLinks, self).get_context_data(**kwargs)

        ctx['title'] = 'Доступные ссылки'
        return ctx


class CreateLinkView(LoginRequiredMixin, CreateView):
    model = Link
    template_name = 'user/create.html'
    fields = ['long', 'short']

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        ctx = super(CreateLinkView, self).get_context_data(**kwargs)

        ctx['title'] = 'Сокращение ссылки'
        return ctx