from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login


from myApp.models import*

def homePage(request):
              
    return render(request,"homePage.html")


def regester(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        if password == confirm_password:
            CustomuserModel.objects.create_user(
                username=username,
                name=name,
                email=email,
                password=password,
                usertype='Principal',
            )
            return redirect("loginPage")
        
    return render(request,"regester.html")

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user=authenticate(username=username, password=password,) 
        if user:
            login(request,user)
            return redirect("homePage")
   
    return render(request,"loginPage.html")

def addTecher(request):
    if request.method=='POST':
        name=request.POST.get("name")
        Subject=request.POST.get("subject")
        phone=request.POST.get("phone")
        address=request.POST.get("address")
        user=CustomuserModel.objects.create_user(
            username=name,
            password=phone,
            usertype="Teacher",
        )
        if user:
            teacherModel.objects.create(
                username=user,
                name=name,
                subjact=Subject,
                phone=phone,
                address=address,
            )
        return redirect("teacherlist")
    return render(request, "addTecher.html")

def teacherlist(request):
    data=teacherModel.objects.all()
    context={
        'data':data
    }
    return render(request, "teacherlist.html",context)
    
def techerdelete(request,myID):
    data=teacherModel.objects.get(id=myID)
    CustomuserModel.objects.get(username=data).delete()
    data.delete()
    return redirect("teacherlist")


