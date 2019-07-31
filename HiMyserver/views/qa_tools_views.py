import YoudaoTranslateClass
import os
from django.http import HttpResponse

homedir = os.path.join(os.path.split(os.path.realpath(__file__))[0], os.path.pardir)


def translateyoudao(request, content):
    youDao = YoudaoTranslateClass.YoudaoTranslate()
    # content = input("请输入翻译语句：")
    result = youDao.youdaoTranslate(content)
    return HttpResponse(result)
