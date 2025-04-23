from datetime import datetime

from django.shortcuts import redirect, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.utils.timezone import now
from django.contrib import messages

from .models import Portfolio, Comment
from .mixins import ThrottlingMixin
from .forms import CommentForm


class HomeListView(ListView):
    model = Portfolio
    template_name = 'index.html'
    context_object_name = 'objects'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()

        context['current_year'] = datetime.now().year

        return context


class ProjectDetailView(DetailView):
    model = Portfolio
    template_name = 'detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        context['form'] = CommentForm()
        context['comments'] = self.object.comments.all()
        context['current_year'] = now().year

        return context


class CommentView(ThrottlingMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'detail.html'
    slug_url_kwarg = 'slug'

    throttle_timeout = 60

    def dispatch(self, request, *args, **kwargs):
        self.portfolio = get_object_or_404(Portfolio, slug=kwargs[self.slug_url_kwarg])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.portfolio = self.portfolio
        messages.success(self.request, "Izohingiz muvaffaqiyatli qo'shildi!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Izoh yuborishda xatolik yuz berdi.")
        return redirect('detail', slug=self.portfolio.slug)

    def get_success_url(self):
        return redirect('detail', slug=self.portfolio.slug).url


class Custom404View(TemplateView):
    template_name = '404.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_year'] = datetime.now().year
        return context
