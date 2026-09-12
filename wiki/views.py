from django.views.generic import ListView, DetailView
from .models import WikiEntry

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