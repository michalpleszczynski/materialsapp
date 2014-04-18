from core.models import Subcategory, Detail


class CutSubcategory(Subcategory):

    class Meta:
        verbose_name = 'Cut subcategory'
        verbose_name_plural = 'Cut subcategories'


class CutDetail(Detail):

    class Meta:
        verbose_name = 'Cut detail'
        verbose_name_plural = 'Cut details'