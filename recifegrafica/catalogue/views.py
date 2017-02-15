from oscar.apps.catalogue.views import *
from oscar.apps.catalogue.views import ProductCategoryView as CoreProductCategoryView
from oscar.core.loading import get_class, get_model

Product = get_model('catalogue', 'product')

class ProductCategoryView(CoreProductCategoryView):
    def get_best_selling(self):
        category = get_object_or_404(Category, pk=self.kwargs['pk'])
        # qs = Product.browsable.base_queryset().select_related('stats').\
        # order_by('-stats__score')[:8].values('categories')
        qs = Product.browsable.base_queryset().select_related('stats').\
        order_by('-stats__score')
        products_to_render = []
        for product in qs:
            product = get_object_or_404(Product, pk=product.id)
            prod_family = product.categories.get(pk=product.categories.values('id'))
            if prod_family.is_child_of(category):
                products_to_render.append(product)

        return products_to_render

    def get_context_data(self, **kwargs):
        context = super(ProductCategoryView, self).get_context_data(**kwargs)
        context['best_products'] = self.get_best_selling()
        return context
