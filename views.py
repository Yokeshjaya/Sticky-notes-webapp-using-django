from django.shortcuts import render
from django.contrib import messages

from .forms import MydoForm
from .models import Mydo

def index(request):
	item_list = Mydo.objects.order_by("-date")
	if request.method == "POST":
		form =MydoForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('Mydo')
	form =MydoForm()

	page={
	        "forms" :form,
	        "list"  :item_list,
	        "title" :"TODO LIST"
	     }
	return render(request, 'index.html',page)


def remove(request,item_id):
	item=Mydo.objects.get(id=item_id)
	item.delete()
	messages.info(request, "item removed !!!")
	return redirect("mydo")