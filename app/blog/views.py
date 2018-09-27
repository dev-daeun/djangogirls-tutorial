from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone

def post_list(request):
    """

    :param request: HTTP 요청 객체
    :return:
    """
    # 리전에 맞는 시간 객체 할당
    current_time = timezone.now()
    return HttpResponse(
        '<html>'
        '<body>'
        '<h1>Post List</h1>'
        '<p>{}<p>'
        '</body>'
        '</html>'.format(current_time.strftime('%Y. %m. %d. %H:%M'))
    )
