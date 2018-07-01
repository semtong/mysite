from django.contrib import admin
from webpage.models import Person

# Register your models here.
# 관리자 페이지에서 유저 관리부분 추가(자동제공)
class PersonAdmin(admin.ModelAdmin):
    pass
# class 와 함계 사용.
# (클래스명, 위에(PersonAdmin)명 입력)
admin.site.register(Person, PersonAdmin)