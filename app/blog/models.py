# external package에 있는 패키지는 루트에 위치한 것처럼 간주한다.
from django.db import models
from django.utils import timezone


class Post(models.Model):
    # 쉼표를 안붙이면 나중에 새 파라미터를 추가하고 깃헙에 커밋할 때 2줄이 추가되므로 마지막 줄 뒤에 쉼표붙이는 게 깃헙에서 보기 깔끔함.
    # 모델의 클래스 속성은 테이블의 컬럼에 대응한다.
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
