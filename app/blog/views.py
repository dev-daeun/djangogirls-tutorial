from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Post


def post_list(request):
    """
    :param request: HTTP 요청 객체
    :return: name
    """
    # 리전에 맞는 시간 객체 할당
    current_time = timezone.now()

    # 템플릿 로더 (루트/templates 에 위치한 템플릿 파일 로드). 로드된 템플릿은 렌더링 해줘야 한다.
    # config/settings.py 에서 TEMPLATES_DIR 경로를 만들고 TEMPLATE 상수에 경로 명시했음.
    # 템플릿 로더가 get_template()으로 파일을 가져올 때 TEMPLATE 상수에 명시된 경로를 참조한다.
    # 각 애플리케이션에서 templates/을 만들 수도 있다. -> 각 애플리케이션에서 템플릿을 참조하도록 해야.

    # template = loader.get_template('blog/post_list.html')
    # context = {
    #     'name': 'kde'
    # }
    # content = template.render(context, request)
    # return HttpResponse(content)

    posts = Post.objects.all().order_by('-published_date')
    page_num = request.GET['page']
    paginator = Paginator(posts, 5)
    try:
        current_page = paginator.page(page_num)
    except PageNotAnInteger:
        # 리퀘스트로 들어온 페이지가 int타입이 아니면 무조건 첫번째 페이지로.
        current_page = paginator.page(1)
    except EmptyPage:
        # 리퀘스트로 들어온 페이지 숫자가 최대를 넘기면 무조건 마지막 페이지로.
        current_page = paginator.page(paginator.num_pages)

    context = {
        'posts': current_page,
    }
    return render(
        request=request,
        context=context,
        template_name='blog/post_list.html',
    )


def post_detail(request, id_):
    # post_detail.html 템플릿에서 kwargs로 넘긴 id가 파라미터로 넘어옴.
    post = Post.objects.get(id=id_)
    context = {
        'post': post
    }
    return render(
        request=request,
        context=context,
        template_name='blog/post_detail.html',
    )


def post_create(request):
    """
    template: blog/post_create.html
    url : /post/create
    :param request: input, textarea, button
    :return: redirect post/[created_post]
    """
    if request.method == 'GET':
        return render(
            request=request,
            template_name='blog/post_create.html',
        )
    else:
        Post.objects.create(
            title=request.POST['title'],
            text=request.POST['content'],
            author=request.user,
        )
        # post/ 로 리다이렉션.
        # redirected = reverse('post_list')
        return HttpResponseRedirect(reverse('post_list'))


def post_edit(request, id_):
    if request.method == 'GET':
        context = {
            'post': Post.objects.get(id=id_)
        }
        return render(
            request=request,
            template_name='blog/post_edit.html',
            context=context
        )
    else:
        updated_title = request.POST['title']
        updated_content = request.POST['content']

        Post.objects.filter(id=id_).update(
            title=updated_title,
            text=updated_content
        )

        # 1. 'post_detail'을 name으로 갖는 뷰 함수로 reverse-resolve.
        # 2. 뷰 함수가 갖는 파라미터를 kwargs로 보낸다. (post_detail 함수는 id_를 파라미터로 받음.)
        # 3. reverse-resolve 한 url으로 리다이렉트 한다.
        return redirect('post_detail', id_=id_)
