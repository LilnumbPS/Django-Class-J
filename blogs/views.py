from datetime import date

from django.db.models import Avg, Max, Min
from django.http import Http404
from django.shortcuts import render, get_object_or_404

from .models import Product

# Create your views here.
all_post=[
    {'slug':'python-programing',
    'title':'python',
    'author':'isavandi',
    'image':'Python.png',
    'date':date(2019,2,18),
    'short_description':'python is open source and high level languages',
    'content':"""Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation. Python is dynamically typed and garbage-collected. It supports multiple programming paradigms, including structured, object-oriented and functional programming.""",
    },
    {'slug':'csharp-programing',
    'title':'C#',
    'author':'tehrani',
    'image':'C#.png',
    'date':date(2019,2,10),
    'short_description':'C# is use by developers',
    'content':"""C# is a general-purpose high-level programming language supporting multiple paradigms. C# encompasses static typing, strong typing, lexically scoped, imperative, declarative, functional, generic, object-oriented, and component-oriented programming disciplines.""",
    },
    {'slug':'php-programing',
    'title':'php',
    'author':'ahmadi',
    'image':'php.png',
    'date':date(2020,10,18),
    'short_description':'php is website',
    'content':"""PHP is a general-purpose scripting language geared towards web development. It was originally created by Danish-Canadian programmer Rasmus Lerdorf in 1993 and released in 1995. The PHP reference implementation is now produced by the PHP Group.""",
    }
]
def get_date(post):
    return post['date']

def index(request):
    # d=list(all_post)
    # context={'a':d}
    # return render(request,'blogs/index.html',context)

    post_sorted=sorted(all_post,key=get_date)
    leatests=post_sorted[-2:]
    return render(request,'blogs/index.html',{'leatests_posts':leatests})

def posts(request):
    return render(request,'blogs/all_post.html',{'all_post':all_post})

def single_post(request,slug):
    post=next(post for post in all_post if post['slug']==slug)
    return render(request,'blogs/post_details.html',{'post':post})

def product_list(request):
    all_product=Product.objects.all().order_by('-price')
    numbers=all_product.count()
    info=all_product.aaggregate(Avg('price'),Max('price'),Min('price'))
    return render(request,'blogs/product_list.html',{'all_product':all_product,
                                                     'numbers':numbers,
                                                     'info':info})

def product_details(request,slug):
    # try:
    #     pro=Product.objects.get(id=product_id)
    # except:
    #     raise Http404
    pro=get_object_or_404(Product,slug=slug)
    return render(request,'blogs/post_details.html',{'pro':pro})