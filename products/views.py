from django.shortcuts import render
from django.views import generic
from django.shortcuts import get_object_or_404
from django.contrib import messages

from .models import Product, Comment
from .forms import CommentForm


class ProductListView(generic.ListView):
    # model = Product
    queryset = Product.objects.filter(active=True)
    template_name = 'products/product_list.html'
    context_object_name = 'products'


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context


class CommentCreateView(generic.CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        product_id = int(self.kwargs['product_id'])
        product = get_object_or_404(Product, id=product_id)
        obj.product = product
        messages.success(self.request, 'Your comment has been successfully registered')
        return super().form_valid(form)


# def product_detail_view(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     product_comment = product.comments.all()
#
#     if request.method == 'POST':
#         comment_form = CommentForm(request.POST)
#         if comment_form.is_valid():
#             new_comment = comment_form.save(commit=False)
#             new_comment.author = request.user
#             new_comment.product = product
#             new_comment.save()
#             comment_form = CommentForm()
#     else:
#         comment_form = CommentForm()
#
#     return render(request, 'products/product_detail.html', {
#         'product': product,
#         'comments': product_comment,
#         'comment_form': comment_form,
#     })
