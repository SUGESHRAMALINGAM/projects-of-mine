from django.shortcuts import render,redirect,reverse
from .models import register,ContainerDetails,LeasingDetails,LesseeDetails
from django.http import HttpResponse

# Create your views here.
def loginpage(request):
    if request.method == 'POST':
        getmail = request.POST.get('username')
        getpassword = request.POST.get('password')
        try:
            register.objects.get(Email=getmail,Password=getpassword)
            return redirect('lessorhome/')
        except:
            return redirect("/login/")
    return render(request,'loginpage.html')

def registerpage(request):
    if request.method == 'POST':
        getname = request.POST.get('Name')
        getgender = request.POST.get('gender')
        getage= request.POST.get('age')
        getmail = request.POST.get('email id')
        getpassword = request.POST.get('password')
        getcountry=request.POST.get('country')
        getcity=request.POST.get('city')
        getnumber=request.POST.get('phoneno')
        users = register()
        users.Name = getname
        users.Gender =getgender
        users.Age = getage
        users.Email =getmail
        users.Password =getpassword
        users.Phone = getnumber
        users.City = getcity
        users.Country = getcountry
        users.save()

    return render(request,'registerpage.html')
def adminpage(request):
    if request.method == 'POST':
        getmail = request.POST.get('username')
        getpassword = request.POST.get('password')
        if getmail == 'admin' and getpassword == '1234':
            return redirect("/adminhome/")
        else:
            return HttpResponse('Invalid')


    return render(request,'adminpage.html')

def adminhome(request):
    return render(request,'adminhome.html')

def lessorhome(request):
    return render(request,'lessorhome.html')

def lessoredit(request):
    lessordetail = register.objects.all()
    return render(request,'lessoredit.html', {'register':lessordetail})

def edit(request,id):
    data=register.objects.get(id=id)
    if request.method == 'POST':
        name=request.POST.get('name')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        phoneno = request.POST.get('phoneno')
        country = request.POST.get('country')
        city = request.POST.get('city')
        password = request.POST.get('password')
        if len(phoneno) == 0 or len(country) == 0 or len(city) == 0 or len(password) == 0:
            return HttpResponse('Please fill the empty fields')
        else:
            data.Name = name
            data.Age = age
            data.Gender = gender
            data.Phone = phoneno
            data.Country = country
            data.City = city
            data.Password = password
            data.save()
    return render(request,'edit.html',{'register':data})
def lessoraddcontainer(request):
    if request.method == 'POST':
        ownerid = request.POST.get('ownerid')
        ownername = request.POST.get('ownername')
        containertype = request.POST.get('containertype')
        containersize = request.POST.get('containersize')
        picture = request.FILES.get('picture')
        quantity = request.POST.get('quantity')
        containeramount = request.POST.get('containeramount')
        containerdata = ContainerDetails()
        if len(ownerid) == 0 or len(ownername) == 0 or len(containertype) == 0 or len(containersize) == 0 or len(
                quantity) == 0 or len(containeramount) == 0:
            return HttpResponse('Please fill the empty feilds')
        else:
            containerdata.Owner_id = ownerid
            containerdata.Owner_Name = ownername
            containerdata.Container_Type = containertype
            containerdata.Container_Size = containersize
            containerdata.Container_Picture = picture
            containerdata.Quantity = quantity
            containerdata.Container_Amount = containeramount
            containerdata.save()
        return redirect('/addcon/')

    return render(request,'lessoraddcontainer.html')

def lessorupdatecontainer(request):
    containerdetail = ContainerDetails.objects.all()
    return render(request, 'luc.html',{'containerdetails':containerdetail})

def lessorupdatecontainer2(request,id):
    containerdetail = ContainerDetails.objects.filter(Status=True)
    updcontainer = ContainerDetails.objects.get(id=id)
    if request.method == 'POST':
        quantity = request.POST.get('quantity')
        containeramount = request.POST.get('containeramount')
        if len(quantity) == 0 or len(containeramount) == 0:
            return HttpResponse('Please fill the empty fields')
        else:
            updcontainer.Quantity = quantity
            updcontainer.Container_Amount = containeramount
            updcontainer.Status = False
            updcontainer.save()
            return redirect('/upcon')
    return render(request, 'uedit.html',{'containerdetail':containerdetail,'updcontainer':updcontainer})
def viewlcon(request):
    leasedcontainer = LeasingDetails.objects.filter(Status=True)
    return render(request,'viewlcontainer.html',{'leasedcontainer':leasedcontainer})

def adminlessorpending(request):
    lp = ContainerDetails.objects.filter(Status=False)
    return render(request,'lessorpending.html', {'ContainerDetails':lp})

def admin_lessorpending_approve(request,id):
    data = ContainerDetails.objects.get(id=id)
    data.Status = True
    data.save()
    return redirect('/lessorpending/')

def admin_lessorapprove(request):
    la= ContainerDetails.objects.filter(Status=True)
    return render(request,'lessorapprove.html',{'la':la})


def lesseelogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            LesseeDetails.objects.get(Username=username, Password=password)
            return redirect('lessee_home/')
        except:
            return HttpResponse('Invalid Username and Password')
    return render(request, 'lesseelogin.html/')


def home_lessee(request):
    return redirect('lesseelogin/')


def lessee_register(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        phoneno = request.POST.get('phoneno')
        company = request.POST.get('company')
        country = request.POST.get('country')
        state = request.POST.get('state')
        city = request.POST.get('city')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')
        lessee = LesseeDetails()
        if len(firstname) == 0 or len(lastname) == 0 or len(email) == 0 or len(phoneno) == 0 or len(
                company) == 0 or len(country) == 0 or len(state) == 0 or len(city) == 0 or len(username) == 0 or len(
                password) == 0 or len(confirmpassword) == 0:
            return HttpResponse('Please fill the all fields')
        elif password != confirmpassword:
            return HttpResponse('password is mismatch')
        else:
            lessee.First_Name = firstname
            lessee.Last_Name = lastname
            lessee.Email = email
            lessee.Phone_No = phoneno
            lessee.Company = company
            lessee.Country = country
            lessee.State = state
            lessee.City = city
            lessee.Username = username
            lessee.Password = password
            lessee.save()
            return redirect('lesseelog/')
    return render(request, 'lesseeregister.html')


def lessee_log_reg(request):
    return redirect('lessee_register/')


def lessee_home(request):
    return render(request, 'lesseehome.html')


def lesseelogout(request):
    return redirect('containerhome/')


def lessee_editprofile(request):
    lesseedetail = LesseeDetails.objects.all()
    return render(request, 'lessee_editprofile.html', {'lesseedetail': lesseedetail})


def lessee_editprofile_edit(request, id):
    lesseedetail = LesseeDetails.objects.all()
    lesseedata = LesseeDetails.objects.get(id=id)
    if request.method == 'POST':
        phoneno = request.POST.get('phoneno')
        country = request.POST.get('country')
        state = request.POST.get('state')
        city = request.POST.get('city')
        password = request.POST.get('password')
        lessee = LesseeDetails()
        if len(phoneno) == 0 or len(country) == 0 or len(state) == 0 or len(city) == 0 or len(password) == 0:
            return HttpResponse('Please fill the empty fields')
        else:
            lesseedata.Phone_No = phoneno
            lesseedata.Country = country
            lesseedata.State = state
            lesseedata.City = city
            lesseedata.Password = password
            lesseedata.save()
            return redirect('lessee_editprofile/')
    return render(request, 'essee_editprofile.html',
                  {'lesseedetail': lesseedetail, 'data': lesseedata})


def lessee_view_container_list(request):
    containerdata = ContainerDetails.objects.filter(Status=True)
    return render(request, 'lessee_viewcontainerlist.html', {'containerdata': containerdata})


def lessee_lease_container(request, id):
    containerdata = ContainerDetails.objects.filter(Status=True)
    leasecontainer = ContainerDetails.objects.get(id=id)
    leasingdata = LeasingDetails()
    if request.method == 'POST':
        lesseeid = request.POST.get('lesseeid')
        lesseename = request.POST.get('lesseename')
        lessorid = request.POST.get('lessorid')
        lessorname = request.POST.get('lessorname')
        containertype = request.POST.get('containertype')
        containersize = request.POST.get('containersize')
        containeramount = request.POST.get('containeramount')
        containerquantity = request.POST.get('containerquantity')
        quantity = request.POST.get('quantity')
        leasingmonths = request.POST.get('leasingmonths')
        date = request.POST.get('date')
        if len(lesseeid) == 0 or len(lesseename) == 0 or len(lessorid) == 0 or len(lessorname) == 0 or len(
                containertype) == 0 or len(containersize) == 0 or len(quantity) == 0 or len(leasingmonths) == 0 or len(
                date) == 0:
            return HttpResponse('Please fill the empty feilds')
        elif int(containerquantity) < int(quantity):
            return HttpResponse('The given number of container quantity is not available')
        else:
            leasingdata.Lessee_id = lesseeid
            leasingdata.Lessee_Name = lesseename
            leasingdata.Owner_id = lessorid
            leasingdata.Owner_Name = lessorname
            leasingdata.Lease_Container_Type = containertype
            leasingdata.Lease_Container_Size = containersize
            leasingdata.Quantity = quantity
            leasingdata.Leasing_Months = leasingmonths
            leasingdata.Lease_Date = date
            leasingdata.Lease_Amount = int(quantity) * float(containeramount) * int(leasingmonths)
            leasecontainer.Quantity = int(containerquantity) - int(quantity)
            leasingdata.save()
            leasecontainer.save()
            return redirect('lessee_view_container_list/')
    return render(request, 'lessee_viewcontainerlist.html',
                  {'containerdata': containerdata, 'leasecontainer': leasecontainer})


def lessee_view_leasing_list(request):
    leasingdata = LeasingDetails.objects.filter(Status=True)
    return render(request, 'lessee_viewleasinglist.html', {'leasingdata': leasingdata})
def admin_lesseepending(request):
    lesseepending = LeasingDetails.objects.filter(Status=False)
    return render(request, 'container_leasing_app/lesseepending.html', {'lesseependingdata':lesseepending})

def admin_lesseepending_approve(request,id):
    data = LeasingDetails.objects.get(id=id)
    data.Status = True
    data.save()
    return redirect('/container_leasing_app/lesseepending')

def admin_lesseeapprove(request):
    lesseeapprove = LeasingDetails.objects.filter(Status=True)
    return render(request, 'container_leasing_app/lesseeapprove.html', {'lesseeapprovedata':lesseeapprove})
