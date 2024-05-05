
from django.shortcuts import render

def welcome_user(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        return render(request, 'welcome/welcome.html', {'name': name})
    return render(request, 'welcome/welcome_form.html')
