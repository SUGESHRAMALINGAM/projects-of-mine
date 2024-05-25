from django.shortcuts import render,redirect,reverse
from .models import LessorDetails,ContainerDetails,LeasingDetails,LesseeDetails
from django.http import HttpResponse

# Create your views here.

# Main page
def ContainerHome(request):
    return render(request, 'container_leasing_app/containerhome.html')

# Admin
def adminlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == 'admin' and password == 'admin':
            return redirect('/container_leasing_app/adminhome')
        else:
            return HttpResponse('Invalid')
    return render(request, 'container_leasing_app/adminlogin.html')

def adminhome(request):
    return render(request, 'container_leasing_app/adminhome.html')

def home_admin(request):
    return redirect('/container_leasing_app/adminlogin')

def adminlogout(request):
    return redirect('/container_leasing_app/containerhome')

def admin_lessorpending(request):
    lessorpending = ContainerDetails.objects.filter(Status=False)
    return render(request, 'container_leasing_app/lessorpending.html', {'lessorpendingdata':lessorpending})

def admin_lessorpending_approve(request,id):
    data = ContainerDetails.objects.get(id=id)
    data.Status = True
    data.save()
    return redirect('/container_leasing_app/lessorpending')

def admin_lessorapprove(request):
    lessorapprove = ContainerDetails.objects.filter(Status=True)
    return render(request, 'container_leasing_app/lessorapprove.html', {'lessorapprovedata':lessorapprove})

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

# Lessor
def lessorlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            LessorDetails.objects.get(Username=username, Password=password)
            return redirect('/container_leasing_app/lessor_home')
        except:
            return HttpResponse('Invalid Username and Password')
    return render(request, 'container_leasing_app/lessorlogin.html')

def home_lessor(request):
    return redirect('/container_leasing_app/lessorlogin')

def lessor_register(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        phoneno = request.POST.get('phoneno')
        country = request.POST.get('country')
        state = request.POST.get('state')
        city = request.POST.get('city')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')
        lessor = LessorDetails()
        if len(firstname) == 0 or len(lastname) == 0 or len(email) == 0 or len(phoneno) == 0 or len(country) == 0 or len(state) == 0 or len(city) == 0 or len(username) == 0 or len(password) == 0 or len(confirmpassword) == 0:
            return HttpResponse('Please fill the all fields')
        elif password != confirmpassword:
            return HttpResponse('password is mismatch')
        else:
            lessor.First_Name = firstname
            lessor.Last_Name = lastname
            lessor.Email = email
            lessor.Phone_No = phoneno
            lessor.Country = country
            lessor.State = state
            lessor.City = city
            lessor.Username = username
            lessor.Password = password
            lessor.save()
            return redirect('/container_leasing_app/lessorlog')
    return render(request, 'container_leasing_app/lessorregister.html')

def lessor_log_reg(request):
    return redirect('/container_leasing_app/lessor_register')

def lessor_home(request):
    return render(request, 'container_leasing_app/lessorhome.html')

def lessorlogout(request):
    return redirect('/container_leasing_app/containerhome')

def lessor_editprofile(request):
    lessordetail = LessorDetails.objects.all()
    return render(request, 'container_leasing_app/lessor_editprofile.html', {'lessordetail':lessordetail})

def lessor_editprofile_edit(request,id):
    lessordetail = LessorDetails.objects.all()
    lessordata = LessorDetails.objects.get(id=id)
    if request.method == 'POST':
        phoneno = request.POST.get('phoneno')
        country = request.POST.get('country')
        state = request.POST.get('state')
        city = request.POST.get('city')
        password = request.POST.get('password')
        if len(phoneno) == 0 or len(country) == 0 or len(state) == 0 or len(city) == 0 or len(password) == 0:
            return HttpResponse('Please fill the empty fields')
        else:
            lessordata.Phone_No = phoneno
            lessordata.Country = country
            lessordata.State = state
            lessordata.City = city
            lessordata.Password = password
            lessordata.save()
            return redirect('/container_leasing_app/lessor_editprofile')
    return render(request, 'container_leasing_app/lessor_editprofile.html', {'lessordetail':lessordetail,'data':lessordata})

def lessor_addcontainer(request):
    if request.method == 'POST':
        ownerid = request.POST.get('ownerid')
        ownername = request.POST.get('ownername')
        containertype = request.POST.get('containertype')
        containersize = request.POST.get('containersize')
        picture = request.FILES.get('picture')
        quantity = request.POST.get('quantity')
        containeramount = request.POST.get('containeramount')
        containerdata = ContainerDetails()
        if len(ownerid) == 0 or len(ownername) == 0 or len(containertype) == 0 or len(containersize) == 0 or len(quantity) == 0 or len(containeramount) == 0:
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
            return redirect('/container_leasing_app/lessor_addcontainer')
    return render(request, 'container_leasing_app/lessor_addcontainer.html')

def lessor_updatecontainer(request):
    containerdetail = ContainerDetails.objects.filter(Status=True)
    return render(request, 'container_leasing_app/lessor_updatecontainer.html',{'containerdetail':containerdetail})

def lessor_updatecontainer_update(request,id):
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
            return redirect('/container_leasing_app/lessor_updatecontainer')
    return render(request, 'container_leasing_app/lessor_updatecontainer.html',{'containerdetail':containerdetail,'updcontainer':updcontainer})

def lessor_view_leased_container(request):
    leasedcontainer = LeasingDetails.objects.filter(Status=True)
    return render(request, 'container_leasing_app/lessor_viewleasedcontainer.html',{'leasedcontainer':leasedcontainer})

# Lessee
def lesseelogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            LesseeDetails.objects.get(Username=username, Password=password)
            return redirect('/container_leasing_app/lessee_home')
        except:
            return HttpResponse('Invalid Username and Password')
    return render(request, 'container_leasing_app/lesseelogin.html')
    
def home_lessee(request):
    return redirect('/container_leasing_app/lesseelogin')

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
        if len(firstname) == 0 or len(lastname) == 0 or len(email) == 0 or len(phoneno) == 0 or len(company) == 0 or len(country) == 0 or len(state) == 0 or len(city) == 0 or len(username) == 0 or len(password) == 0 or len(confirmpassword) == 0:
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
            return redirect('/container_leasing_app/lesseelog')
    return render(request, 'container_leasing_app/lesseeregister.html')

def lessee_log_reg(request):
    return redirect('/container_leasing_app/lessee_register')

def lessee_home(request):
    return render(request, 'container_leasing_app/lesseehome.html')
    
def lesseelogout(request):
    return redirect('/container_leasing_app/containerhome')

def lessee_editprofile(request):
    lesseedetail = LesseeDetails.objects.all()
    return render(request, 'container_leasing_app/lessee_editprofile.html',{'lesseedetail':lesseedetail})

def lessee_editprofile_edit(request,id):
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
            return redirect('/container_leasing_app/lessee_editprofile')
    return render(request, 'container_leasing_app/lessee_editprofile.html',{'lesseedetail':lesseedetail,'data':lesseedata})

def lessee_view_container_list(request):
    containerdata = ContainerDetails.objects.filter(Status=True)
    return render(request, 'container_leasing_app/lessee_viewcontainerlist.html', {'containerdata':containerdata})

def lessee_lease_container(request,id):
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
        if len(lesseeid) == 0 or len(lesseename) == 0 or len(lessorid) == 0 or len(lessorname) == 0 or len(containertype) == 0 or len(containersize) == 0 or len(quantity) == 0 or len(leasingmonths) == 0 or len(date) == 0:
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
            return redirect('/container_leasing_app/lessee_view_container_list')
    return render(request, 'container_leasing_app/lessee_viewcontainerlist.html', {'containerdata':containerdata, 'leasecontainer':leasecontainer})

def lessee_view_leasing_list(request):
    leasingdata = LeasingDetails.objects.filter(Status=True)
    return render(request, 'container_leasing_app/lessee_viewleasinglist.html',{'leasingdata':leasingdata})
