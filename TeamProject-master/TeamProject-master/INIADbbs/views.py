from django.shortcuts import render,redirect,get_object_or_404
from django.views.decorators.http import require_POST
from.models import Message
from.forms import MessageForm

def index(request):
    """一覧画面"""
    d = {
    'messages':Message.objects.all(),
        }
    return render(request,'INIADbbs/index.html',d)
def create(request):
    """登録一覧"""
    form = MessageForm(request.POST or None)
    if form.is_valid():
        Message.objects.create(**form.cleaned_data)
        return redirect('index')

    e = {
        'form':form,
        }
    return render(request,'INIADbbs/create.html', e)

def edit(request,editing_id):
    """編集一覧"""
    message = get_object_or_404(Message,id=editing_id)
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message.message = form.cleaned_data['message']
            message.save()
            return redirect('index')
    else:
        form = MessageForm({'message':message.message})
    f = {
        'form':form,
    }
    return render(request,'INIADbbs/create.html',f)

@require_POST
def delete(request):
    """削除処理"""
    delete_ids = request.POST.getlist('delete_ids')
    if delete_ids:
        Message.objects.filter(id__in=delete_ids).delete()
    return redirect('index')
# Create your views here.
