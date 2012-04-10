from django import forms
from django.utils.safestring import mark_safe

#An interest value of this would be x.object
LOOKUP_IMAGE = lambda x: '<img src="/static/admin/img/admin/selector-search.gif" style="cursor: pointer; margin-left: 5px" width="16" height="16" alt="Lookup">'


class ModelLinkWidget(forms.Widget):
    def __init__(self, obj, attrs=None):
        self.object = obj
        super(ModelLinkWidget, self).__init__(attrs)

    def render(self, name, value, attrs=None):
        if self.object.pk:
            return mark_safe(
                u'<a target="_blank" href="../../../%s/%s/%s/">%s</a>' %\
                      (
                       self.object._meta.app_label,
                       self.object._meta.object_name.lower(),
                       self.object.pk, LOOKUP_IMAGE(self)
                       )
            )
        else:
            return mark_safe(u'')


class SelectWithLinkWidget(forms.widgets.Select):
    def __init__(self, klass, attrs=None, choices=(), *args, **kwargs):
        self.klass = klass
        super(SelectWithLinkWidget, self).__init__(attrs, choices, *args, **kwargs)

    def render(self, *args, **kwargs):
        result = super(SelectWithLinkWidget, self).render(*args, **kwargs)
        name, value = args
        if not value:
            return result
        return mark_safe(result +
                u'<a target="_blank" href="../../../%s/%s/%s/">%s</a>' %\
                      (
                       self.klass._meta.app_label,
                       self.klass._meta.object_name.lower(),
                       value, LOOKUP_IMAGE(self)
                       )
        )
