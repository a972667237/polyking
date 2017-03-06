from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Things
from .form import AddForm
from django.utils import timezone

def index(request):
    latest_todo_list = Things.objects.order_by('-add_date')[:5]
    context = {
        'latest_todo_list': latest_todo_list,
    }
    return render(request, 'todo/index.html', context)


def new(request):
    if request.method == 'POST':#提交请求时才会访问这一段，首次访问页面时不会执行
        form = AddForm(request.POST)
        if form.is_valid():
            q = Things(thing_text=form.a, add_date=timezone.now())
            q.save
            return HttpResponseRedirect('/')
    else:#首次访问该url时没有post任何表单
        form = AddForm()
    return render(request, 'todo/add.html', {'form': form})


