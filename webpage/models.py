from django.db import models

# Create your models here.

class Person(models.Model):
    # 데이터베이스 컬럼 설정
    """
    https://docs.djangoproject.com/en/2.0/ref/models/fields/#datetimefield
    models.~~~부분 관련 api Document 문서 참조

    """
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(null=True)
    updateDate = models.DateTimeField(null=True)

    # 관리자 페이지 표기방법 설정
    def __str__(self):
        # 성을 표기하고 뒤에 이름을 표현 ex.조 현은
        return "%s %s" % (self.last_name, self.first_name)