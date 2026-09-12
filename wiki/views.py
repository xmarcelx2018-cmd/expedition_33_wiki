from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from .models import WikiEntry
from .forms import WikiEntryForm


class WikiList(ListView):
    """
    Display Wiki entries for a specific category.
    """
    category = None
    model = WikiEntry
    template_name = 'wiki/wiki_list.html'
    context_object_name = 'wiki_entries'

    def get_queryset(self):
        return WikiEntry.objects.filter(category=self.category)


class WikiDetail(DetailView):
    """
    Display a single Wiki entry.
    """
    model = WikiEntry
    template_name = 'wiki/wiki_detail.html'
    context_object_name = 'wiki_entry'


class WikiCreate(LoginRequiredMixin, CreateView):
    """
    Allow logged-in users to create a Wiki entry.
    """
    model = WikiEntry
    form_class = WikiEntryForm
    template_name = 'wiki/wiki_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return f'/wiki/{self.object.pk}/'