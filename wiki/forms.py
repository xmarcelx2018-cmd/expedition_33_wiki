from django import forms
from .models import WikiEntry


class WikiEntryForm(forms.ModelForm):

    class Meta:
        model = WikiEntry
        fields = ['title', 'category', 'content', 'image']

    def clean_title(self):
        title = self.cleaned_data['title'].strip()

        if len(title) < 3:
            raise forms.ValidationError(
                "Title must be at least 3 characters long."
            )

        return title

    def clean_content(self):
        content = self.cleaned_data['content'].strip()

        if len(content) < 10:
            raise forms.ValidationError(
                "Content must be at least 10 characters long."
            )

        return content