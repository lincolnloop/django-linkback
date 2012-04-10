from django import forms
from django.utils.safestring import mark_safe

#An interest value of this would be x.object
LOOKUP_IMAGE = lambda x: '<img src="/static/admin/img/admin/selector-search.gif" style="cursor: pointer; margin-left: 5px" width="16" height="16" alt="Lookup">'


class SelectWithLinkWidget(forms.widgets.Select):
    def __init__(self, klass, attrs=None, choices=(), *args, **kwargs):
        self.klass = klass
        super(SelectWithLinkWidget, self).__init__(attrs, choices, *args, **kwargs)

    def render(self, *args, **kwargs):
        result = super(SelectWithLinkWidget, self).render(*args, **kwargs)
        name, value = args
        return mark_safe(result +
                u'<a target="_blank" href="../../../%s/%s/%s/">%s</a>' %\
                      (
                       self.klass._meta.app_label,
                       self.klass._meta.object_name.lower(),
                       value, LOOKUP_IMAGE(self)
                       )
        )

        return result
