from django import forms

from .widgets import ModelLinkWidget


class LinkBackForm(forms.ModelForm):
    # required=False is essential cause we don't
    # render input tag so there will be no value submitted.
    link = forms.CharField(label='link', required=False)

    def __init__(self, *args, **kwargs):
        super(LinkBackForm, self).__init__(*args, **kwargs)
        # instance is always available, it just does or doesn't have pk.
        self.fields['link'].widget = ModelLinkWidget(self.instance)
