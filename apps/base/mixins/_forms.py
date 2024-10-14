from django.forms import ModelForm


class BaseForm(ModelForm):
    """Base form for all forms in the project"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "input"})
