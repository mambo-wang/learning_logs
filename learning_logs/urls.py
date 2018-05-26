"""定义learning_logs的URL模式"""

from django.conf.urls import url
from . import views

urlpatterns = [

    # r让Python将接下来的字符串视为原始字符串，而引号告诉Python正则表达式始于和终于何处，^让Python查看字符串的开头，
    # 美元符号让Python查看字符串的结尾
    # 总体而言，这个正则表达式让Python查找开头和末尾之间没有任何东
    # 西的URL。Python忽略项目的基础URL（http://localhost:8000/），因此这个正则表达式与基础URL
    # 匹配。其他URL都与这个正则表达式不匹配
    url(r'^$', views.index, name='index')
]