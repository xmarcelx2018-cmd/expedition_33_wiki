from django import forms
from .models import WikiEntry


class WikiEntryForm(forms.ModelForm):

    class Meta:
        model = WikiEntry
        fields = ['title', 'category', 'content', 'image']
        widgets = {
            'title': forms.TextInput(attrs={
                'id': 'wiki-title',
            }),
            'content': forms.Textarea(attrs={
                'id': 'wiki-content',
            }),
            'image': forms.FileInput(),
        }

    def clean_title(self):
        title = self.cleaned_data['title'].strip()

        if len(title) < 3:
            raise forms.ValidationError(
                "Title must be at least 3 characters long."
            )

        if len(title) > 50:
            raise forms.ValidationError(
                "Title cannot be more than 50 characters long."
            )

        return title

    def clean_content(self):
        content = self.cleaned_data['content'].strip()

        if len(content) < 10:
            raise forms.ValidationError(
                "Content must be at least 10 characters long."
            )

        if len(content) > 3000:
            raise forms.ValidationError(
                "Content cannot be more than 3000 characters long."
            )

        return content