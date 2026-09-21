from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
     return render(request, 'usuarios/home.html', context= {
    'eh_suporte': request.user.groups.filter(name='Suporte').exists()
})