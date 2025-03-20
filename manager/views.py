from datetime import datetime

from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from django.utils.timezone import now
from django.contrib import messages

from .models import Portfolio
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

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.portfolio = self.object
            comment.save()

            messages.success(request, "Izohingiz muvaffaqiyatli qo‘shildi!")
            return redirect('detail', slug=self.object.slug)

        return self.render_to_response(self.get_context_data(form=form))