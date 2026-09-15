from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import WikiEntry
from .forms import WikiEntryForm

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Registration successful! You can now log in."
            )
            return redirect("login")
    else:
        form = UserCreationForm()

    return render(
        request,
        "registration/register.html",
        {"form": form}
    )


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
        messages.success(self.request, "Wiki entry created successfully!")
        return super().form_valid(form)

    def get_success_url(self):
        return f'/wiki/{self.object.pk}/'


class WikiUpdate(LoginRequiredMixin, UpdateView):
    """
    Allow the author of a Wiki entry to edit it.
    """
    model = WikiEntry
    form_class = WikiEntryForm
    template_name = 'wiki/wiki_edit.html'

    def get_queryset(self):
        return WikiEntry.objects.filter(author=self.request.user)

    def form_valid(self, form):
        messages.success(self.request, "Wiki entry updated successfully!")
        return super().form_valid(form)

    def get_success_url(self):
        return f'/wiki/{self.object.pk}/'


class WikiDelete(LoginRequiredMixin, DeleteView):
    """
    Allow the author of a Wiki entry to delete it.
    """
    model = WikiEntry
    template_name = 'wiki/wiki_delete.html'
    context_object_name = 'wiki_entry'

    def get_queryset(self):
        return WikiEntry.objects.filter(author=self.request.user)

    def form_valid(self, form):
        messages.success(self.request, "Wiki entry deleted successfully!")
        return super().form_valid(form)

    def get_success_url(self):
        category = self.object.category

        if category == 'character':
            return '/wiki/characters/'
        elif category == 'weapon':
            return '/wiki/weapons/'
        elif category == 'location':
            return '/wiki/locations/'

        return '/wiki/characters/'

def home(request):
        return render(request, "wiki/home.html")