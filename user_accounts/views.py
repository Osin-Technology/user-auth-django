from django.shortcuts import render, HttpResponse

from django.contrib.auth.models import User
# Create your views here.

def register(request):
    template_path = "user_accounts/register.html"
    context = {}

    if request.method == "GET":
        return render(request, template_path)
    
    if request.method == "POST":
        data = request.POST.copy().dict()
        
        print(data)

        if data['password'] == data['password2']:
            name = data['name'].split(' ')
            
            # adding data
            data['first_name'] = name[0]
            data['last_name'] = name[1]
            data['username'] = data['email'].split('@')[0]
            # data['password'] = make_password(data['password'])

            # removing data
            data.pop('name')
            data.pop('csrfmiddlewaretoken')
            data.pop('password2')

            User.objects.create_user(**data)

            return HttpResponse('successfully registered.')
        else:
            context['error'] = 'Passwords Do not Match'
            return render(request, template_path, context)
