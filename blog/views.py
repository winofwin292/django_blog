from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Category, Blog, Comment, Contact
from .forms import CommentForm, ContactForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.


def index(request):
    posts = Blog.objects.filter(status=1).order_by('-posted')[:3]
    contact_form = ContactForm()
    context = dict(posts=posts, contact=contact_form)
    return render(request, 'index.html', context)


def post_detail(request, slug):
    post = get_object_or_404(Blog, slug=slug)
    comments = Comment.objects.filter(blog=post)

    recent_posts = Blog.objects.filter(status=1).order_by('-posted')[:5]
    categories = Category.objects.all()

    context = dict(post=post, comments=comments, form=CommentForm(), recent_posts=recent_posts,
                   categories=categories)
    return render(request, 'view_post.html', context)


def all_post(request):
    posts = Blog.objects.all()
    paginator = Paginator(posts, 8)
    page = request.GET.get('page', 1)
    try:
        posts_paged = paginator.page(page)
    except PageNotAnInteger:
        posts_paged = paginator.page(1)
    except EmptyPage:
        posts_paged = paginator.page(paginator.num_pages)

    recent_posts = Blog.objects.filter(status=1).order_by('-posted')[:5]
    categories = Category.objects.all()

    context = dict(posts=posts_paged, recent_posts=recent_posts, categories=categories)

    return render(request, 'all_post.html', context)


def get_post_by_category(request, category_slug):
    category = Category.objects.get(slug=category_slug)
    posts_by_category = Blog.objects.filter(category=category)
    paginator = Paginator(posts_by_category, 8)
    page = request.GET.get('page', 1)
    try:
        posts_paged = paginator.page(page)
    except PageNotAnInteger:
        posts_paged = paginator.page(1)
    except EmptyPage:
        posts_paged = paginator.page(paginator.num_pages)

    recent_posts = Blog.objects.filter(status=1).order_by('-posted')[:5]
    categories = Category.objects.all()

    context = dict(category_title=category.title, posts=posts_paged, recent_posts=recent_posts, categories=categories)

    return render(request, 'post_by_category.html', context)


def add_comment_save(request, slug):
    if request.method != "POST":
        return HttpResponse("Lỗi phương thức")
    else:
        form = CommentForm(request.POST)
        post = Blog.objects.get(slug=slug)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            body = form.cleaned_data['body']
            comment = Comment.objects.create(name=name, email=email, blog=post, body=body)
            comment.save()
            return redirect('/' + post.slug + '#box-comments')
        else:
            return redirect('/' + post.slug + '#box-comments')


def search_post(request):
    if request.method != "POST":
        return HttpResponse("Lỗi phương thức")
    else:
        find_keyword = request.POST.get('keyword')
        title_results = Blog.objects.filter(title__contains=find_keyword)
        body_results = Blog.objects.filter(body__contains=find_keyword)
        list_result = []
        for result in title_results:
            list_result.append(result)

        for result in body_results:
            list_result.append(result)

        paginator = Paginator(list_result, 8)
        page = request.GET.get('page', 1)
        try:
            result_paged = paginator.page(page)
        except PageNotAnInteger:
            result_paged = paginator.page(1)
        except EmptyPage:
            result_paged = paginator.page(paginator.num_pages)

        recent_posts = Blog.objects.filter(status=1).order_by('-posted')[:5]
        categories = Category.objects.all()

        context = dict(results=result_paged, keyword=find_keyword, recent_posts=recent_posts, categories=categories)

        return render(request, 'search_post.html', context)


def add_contact_save(request):
    if request.method != "POST":
        return HttpResponse("Lỗi phương thức")
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            body = form.cleaned_data['body']
            contact = Contact.objects.create(name=name, email=email, body=body)
            contact.save()
            return render(request, 'thank.html', {'msg': 'Cảm ơn bạn đã để lại tin nhắn'})
        else:
            return render(request, 'thank.html', {'msg': 'Thao tác lỗi'})


def error(request, exception):
    return render(request, 'error.html', {'message': exception})
