from django.shortcuts import render


# Create your views here.
def index(request):
    """学习笔记的主页"""
    # 两个参数分别为原始请求对象和可用于创建网页的模板
    return render(request, 'learning_logs/index.html')