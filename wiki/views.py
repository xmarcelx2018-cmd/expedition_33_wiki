from django.views.generic import ListView
from .models import WikiEntry


class WikiList(ListView):
    """
    Display all Wiki entries.
    """
    model = WikiEntry
    template_name = 'wiki/wiki_list.html'
    context_object_name = 'wiki_entries'