from django.shortcuts import render
from .models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def home(request):
    stud = User.objects.all()
    context = {'stud':stud}
    return render(request, 'enroll/home.html', context)

#@csrf_exempt
def save_data(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email'] 
        password = request.POST['password']   
        usr= User(name = name, email = email, password = password)  
        usr.save()
        stu = User.objects.values()
        student_data = list(stu)
        return JsonResponse({'status':'save','student_data':student_data})
    else:
        return JsonResponse({'status':0})  


# def edit_data(request):
#     if request.method == "POST":
#         id = request.POST.get('sid')
#         updated = User.objects.get(pk=id)
#         deleted.delete()
#         return JsonResponse({'status':1})

#     else:
#         return JsonResponse({'status':0})            



def delete_data(request):
    if request.method == "POST":
        id = request.POST.get('sid')
        deleted = User.objects.get(pk=id)
        deleted.delete()
        return JsonResponse({'status':1})

    else:
        return JsonResponse({'status':0})            
