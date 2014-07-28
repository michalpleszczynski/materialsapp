# coding: utf-8
from __future__ import unicode_literals


class DropNullMixin(object):
    """
    Don't return null values.
    """
    def dehydrate(self, bundle):
        if isinstance(bundle.data, dict):
            bundle.data = dict([item for item in bundle.data.items()
                                if item[1] is not None and item[1] != ""])
        return bundle


class DetailMixin(object):
    """
    Fields in Resource.Meta.detail_fields won't be displayed on a list view.
    """
    def __init__(self, api_name=None):
        super(DetailMixin, self).__init__(api_name)
        detail_fields = getattr(self._meta, 'detail_fields', [])
        if detail_fields:
            for name, field in self.fields.items():
                if name in detail_fields:
                    field.use_in = 'detail'