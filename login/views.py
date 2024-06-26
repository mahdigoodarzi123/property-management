from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import UploadFileForm
import os
from django.conf import settings
from add_product.models import Product
from django.db.models import Q
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login
from django.urls import reverse_lazy

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect(reverse_lazy('main_page'))
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})



@login_required
def main_page(request):
    sort_by = request.GET.get('sort_by', 'code')
    order = request.GET.get('order', 'asc')
    query = request.GET.get('query', '')

    if query:
        products = Product.objects.filter(
            Q(code__icontains=query) |
            Q(group__icontains=query) |
            Q(description__icontains=query) |
            Q(location__icontains=query) |
            Q(floor__icontains=query) |
            Q(status__icontains=query) |
            Q(census_1403__icontains=query) |
            Q(room__icontains=query) |
            Q(user__icontains=query) |
            Q(vendor__icontains=query) |
            Q(notes__icontains=query)
        )
    else:
        products = Product.objects.all()

    if order == 'asc':
        products = products.order_by(sort_by)
    else:
        products = products.order_by(f'-{sort_by}')

    return render(request, 'main_page.html', {
        'username': request.user.username,
        'products': products,
        'sort_by': sort_by,
        'order': order,
        'query': query
    })




def upload_file_view(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # پردازش فایل اینجا
            uploaded_file = request.FILES['file']


            file_path = os.path.join(settings.MEDIA_ROOT, uploaded_file.name)
            
            with open(file_path, 'wb+') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)

            # انجام عملیات مورد نیاز با فایل، مثلاً ذخیره یا پردازش
            return render(request, 'upload_success.html', {'filename': uploaded_file.name})
    else:
        form = UploadFileForm()
    return render(request, 'upload_file.html', {'form': form})
