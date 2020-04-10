from django.shortcuts import HttpResponse, get_object_or_404, redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .forms import createForm



# import model
from . models import Author
from . models import BookList,Userprofile,BookLoan
from django.http import Http404

# Create your views here.



def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                auth.login(request, user)
                return redirect('/')
            else:
                return redirect('disabled account')

        else:
            return redirect('/invalid')

    else:
        return render(request, 'login.html')
        





# Registration View
def registration(request):
    
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username taken ')
                return redirect (request, 'registration')

            elif User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                return redirect ('registration')
                

            else:
                user= User.objects.create_user(username= username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                
                messages.info(request, 'user created')
                return redirect ('login')
                

        else:
            messages.info(request, 'password not matching')
            return redirect ('registration')
        


    else:
        return render(request,'registration.html')
        



def home(request):
    booklists = BookList.objects.all()

    return render(request, 'library.html', {'booklists':booklists,} )

def logout(request):
    auth.logout(request)
    return redirect('/')

def ShowBook(request, id):
    if request.method == "GET":
        showbooks = BookList.objects.get(pk=id)
        booklists = BookList.objects.all().order_by('-id')[:4]
        return render(request, 'showbook.html', {'showbooks':showbooks,'booklists':booklists } )
    else:
        try:
            bookInstance=get_object_or_404(BookList, id=id)
            myObj=BookLoan.objects.create(user=request.user, Book=bookInstance)
            myObj.save()
            #return redirect('showbook', id=id)
            return redirect('order')
            
        except:
            return Http404("No book found to save")




def Profile(request):
    #post= Userprofile.objects.all()
    posts= BookLoan.objects.filter(user= request.user.id)
    

    

    if request.method == 'POST':
        
        form = createForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = createForm()
    return render(request, 'profile.html', {
        
        'posts':posts,
        'form':form,
    })


    #return render(request, 'profile.html',{'posts':posts} )






def order(request):
    
    posts= BookLoan.objects.filter(user= request.user.id).order_by('-id')

    return render(request, 'order.html',{'posts':posts} )











    





