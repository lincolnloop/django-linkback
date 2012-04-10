from .widgets import SelectWithLinkWidget


class LinkBackMixin(object):
    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        try:
            kwargs['widget'] = SelectWithLinkWidget(db_field.rel.to)
        except TypeError:  # django 1.4+
            kwargs['widget'] = SelectWithLinkWidget(db_field.rel.to, self.admin_site)
        return db_field.formfield(**kwargs)
