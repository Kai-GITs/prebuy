from django.forms import ModelForm
from main.models import News
from django.utils.html import strip_tags

class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ["name", "description", "category", "thumbnail", "is_featured", "price"]
    
    def clean_title(self):
        title = self.cleaned_data["name"]
        return strip_tags(title)

    def clean_content(self):
        content = self.cleaned_data["description"]
        return strip_tags(content)