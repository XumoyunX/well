from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
import random

from main.models import Category, Product, Kontak


def home(requset):
    category = Category.objects.all()
    product = Product.objects.all()
    products = []
    # for i in range(2):
        # products.append(random.choice(product))
    if product.exists():

        ran = len(product)
        for _ in range(11):
            index = random.randint(0,ran)
            products.append(product[index])

            # print(products)
        # max_id = Product.objects.order_by('-id')[:0]
        # product = random.randint(int(max_id) + 1)
        # product = Product.objects.filter(id__gte=random_id)[:0]
        # gar= Gallery.objects.order_by()[:2]

        print(category)
        print(product,'A')
        ctx = {
            'category':category,
            'product':products,
            # 'gar': gar,
            'h_active':'active'
        }
    else:
        ctx = {
            'category': category,
            'product': products,
            # 'gar': gar,
            'h_active': 'active'
        }
    return render(requset,'main/index.html',ctx)

# class MainIndex(TemplateView):
#     template_name = "main/index.html"
#
#     def get(self, request, pk):
#         category = Category.objects.all()
#         a = Product.objects.get(category_id=id)
#         print(a)
#         ctx ={
#             'category':category,
#             'product':a
#         }
#         return render(request,'main/index.html',ctx)

    # def get_context_data(self, **kwargs):
    #     kwargs["category"] = Category.objects.all()
    #     kwargs["product"] = Product.objects.all()
    #
    #     return super().get_context_data(**kwargs)


class Menu(View):
    def get(self, request):
        category = Category.objects.all()
        product = Product.objects.all()
        ctx = {
            'category':category,
            'product':product,
            'm_active':'active'
        }
        return render(request,'layouts/menu.html',ctx)





class Pro(TemplateView):
    template_name = "layouts/index2.html"

    def get_context_data(self, **kwargs):
        kwargs["gar"] = Kontak.objects.all()


        return super().get_context_data(**kwargs)



class About(View):
    def get(self, request):
        category = Category.objects.all()
        product = Product.objects.all()
        products = []
        # for i in range(2):
        # products.append(random.choice(product))
        if product.exists():
            ran = len(product)
            for _ in range(11):
                index = random.randint(0, ran)
                products.append(product[index])

            ctx = {
                'category': category,
                'product': products,
                'a_active':'active'

            }
        else:
            ctx = {
                'category': category,
                'product': products,
                'a_active': 'active'
            }
        return render(request, 'layouts/about.html', ctx)





class Con(TemplateView):
    template_name = "layouts/contact.html"

    def get_context_data(self, **kwargs):
        kwargs['gar'] = Kontak.objects.all()


        return super().get_context_data(**kwargs)




#
# class Pro(View):
#     def get(self, request, pk):
#         category = Category.objects.all()
#         a = Product.objects.get(category_id=id)
#         print(a)
#         ctx ={
#             'category':category,
#             'product':a
#         }
#         return render(request,'main/index.html',ctx)