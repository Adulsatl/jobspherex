from django.shortcuts import render,redirect
from .models import*
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import FileResponse
# from django.contrib.auth.hashers import check_password

def home(request):
    return render(request,'home_page.html')

def c_reg(request):
    if request.method=='POST':
        companyname=request.POST['cname']
        email=request.POST['mail']
        number=request.POST['num']
        password=request.POST['cpassd']
        location=request.POST['location']
        licence=request.POST['licence']
        industry=request.POST['industry']
        year=request.POST['year']
        if password==password:
            user=None
            if User.objects.filter(username=companyname).exists():
                user=User.objects.get(username=companyname)
                if reg.objects.filter(user=user).exists():
                    return redirect(c_reg)
            else:
                User.objects.create_user(username=companyname,password=password,email=email).save()
                user=User.objects.get(username=companyname)
            if user:
                if company_reg.objects.filter(c_name=companyname):
                    return render(request,'company_reg.html',{'key1':'Username already exists'})        
                else:
                    company_reg(user=user,c_name=companyname,c_email=email,c_number=number,c_password=password,c_location=location,c_licence=licence,c_industry=industry,c_year=year).save()
                    return redirect(c_login)
        else:   
            return render(request,'company_reg.html')
    else:
        return render(request,'company_reg.html')
    return render(request,'company_reg.html')

def c_login(request):
    if request.method=='POST':
        username=request.POST['cuser']
        password=request.POST['cpass']
        if company_reg.objects.filter(c_name=username,c_password=password).exists():
            u=auth.authenticate(username=username,password=password)
            if u is not None:
                auth.login(request,u)
                return redirect(c_details)
            else:
                return render(request,'company_login.html')
        else:
            return render(request,'company_login.html')
    return render(request,'company_login.html')

def c_details(request):
    return render(request,'company_details.html')

def form(request):
    print(request.user)
    # users=User.objects.get(username=request.user)
    # print(users)
    com_users=company_reg.objects.get(user=request.user)
    print(com_users)
    if request.method=='POST':
        job_detail=request.POST['job']
        job_description=request.POST['description']
        company_names=request.POST['name']
        skill=request.POST['skill'] 
        experiences=request.POST['exp']
        qualification=request.POST['qua'] 
        benifits=request.POST['benifit']
        pay_types=request.POST['pay']
        salary=request.POST['sal']
        date=request.POST['date']
        job(user=com_users,job_details=job_detail,job_description=job_description,company_name=company_names,skills=skill,experience=experiences,qualification=qualification,benifits=benifits,pay_types=pay_types,salary=salary,date=date).save()
        return redirect(c_details)
    return render(request,'company_form.html',{'key9':com_users})

def company_profiles(request):
    value=company_reg.objects.get(user=request.user)
    return render(request,'company_profile.html',{'key3':value})

def applicant_details(request,pk):
    application=applicant_form.objects.filter(job=pk)
    return render(request,'applicant_detail.html',{'key':application})

def update(request):
    updateval=company_reg.objects.get(user=request.user)
    udate=User.objects.get(id=updateval.user.id)
    if request.method=='POST':
        updateval.c_name=request.POST['name']
        updateval.c_email=request.POST['mail']
        updateval.c_number=request.POST['num']
        updateval.c_location=request.POST['location']
        updateval.c_licence=request.POST['Licence']
        updateval.c_industry=request.POST['Industry']
        updateval.c_year=request.POST['year']
        updateval.save()
        udate.username=request.POST['name']
        udate.email=request.POST['mail']
        udate.save()
        return redirect(c_details)
    return render(request,'company_update.html',{'key5':updateval})

def cjob_list(request):
    users=company_reg.objects.get(user=request.user)
    print(users)
    v=job.objects.filter(user=users).order_by('-id')
    print(len(v))
    return render(request,'job_list.html',{'key6':v})

@login_required(login_url='log')
def change_password(request):
    valu=company_reg.objects.get(user=request.user)
    var=User.objects.get(id=valu.user.id)
    if request.method == 'POST':
        valu.c_password=request.POST['new_password']
        valu.save()
        pwd=request.POST['new_password']
        var.set_password(pwd)
        var.save()
        return redirect(c_login)
    return render(request,'change_password.html')

def resume(request,pk):
    filepath=applicant_form.objects.get(id=pk).resume.path
    return FileResponse(open(filepath,'rb'),content_type='application/pdf')

def u_reg(request):
    if request.method=='POST':
        firstname=request.POST['ftname']
        lastname=request.POST['ltname']
        email=request.POST['mail1']
        number=request.POST['num1']
        username=request.POST['usern']
        password=request.POST['upassd']
        image=request.FILES['img']
        if password==password:
            user=None
            if User.objects.filter(username=username).exists():
                user=User.objects.get(username=username)
                if company_reg.objects.filter(user=user).exists():
                    return render(request,'user_reg.html',{'key2':'Already exists'})
            else:
                User.objects.create_user(username=username,password=password,first_name=firstname,last_name=lastname,email=email).save()
                user=User.objects.get(username=username)
            if user:
                if reg.objects.filter(u_username=username):
                    return render(request,'user_reg.html',{'key1':'Username already exists'})
                else:
                    reg(user=user,u_firstname=firstname,u_lastname=lastname,u_email=email,u_number=number,u_username=username,u_password=password,u_image=image).save()
                    return redirect(u_login)
        else:
            return render(request,'user_reg.html',{'key':'Successfully Registered'})       
    return render(request,'user_reg.html')

def u_login(request):
    if request.method=='POST':
        username=request.POST['uuser']
        password=request.POST['upass']
        if reg.objects.filter(u_username=username,u_password=password).exists():
            u=auth.authenticate(username=username,password=password)
            if u is not None:
                auth.login(request,u)
                return redirect(u_job)
            else:
                return render(request,'user_login.html')
        else:
            return render(request,"user_login.html")
    return render(request,'user_login.html')                


@login_required(login_url='logi')
def u_profile(request):
    profile=reg.objects.get(user=request.user)
    return render(request,'u_profile.html',{'key':profile})

@login_required(login_url='logi')
def u_update(request):
    values=reg.objects.get(user=request.user)
    val=User.objects.get(id=values.user.id)
    if request.method=='POST':
        values.u_firstname=request.POST['fisrtname']
        values.u_lastname=request.POST['lastname']
        values.u_email=request.POST['email']
        values.u_number=request.POST['number']
        values.u_username=request.POST['username']
        values.save()
        val.username=request.POST['username']
        val.email=request.POST['email']
        val.save()
        return redirect(u_profile)
    return render(request,'u_update.html',{'key':values})

@login_required(login_url='logi')
def u_job(request):
    a=job.objects.all().order_by('-id')
    return render(request,'u_jobs.html',{'key':a})

@login_required(login_url='logi')
def search(request):
    if request.method=='POST':
        searches=request.POST['search_me']
        values=job.objects.filter(job_details=searches)
    return render(request,'u_jobs.html',{'key':values})

@login_required(login_url='logi')
def uchange_password(request):
    valu=reg.objects.get(user=request.user)
    var=User.objects.get(id=valu.user.id)
    if request.method == 'POST':
        # current_password=request.POST['current_password']
        # new_password=request.POST['new_password']
        # confirm_password=request.POST['confirm_password']
        # if check_password(current_password,confirm_password):
        #     if current_password != new_password :
        #         if new_password==confirm_password:
        valu.u_password=request.POST['new_password']
        valu.save()
        pwd=request.POST['new_password']
        var.set_password(pwd)
        var.save()
        return redirect(u_login)
        #         else:
        #             return render(request, {'key':'The new passwords do not match.'})
        #     else:
        #         return render(request, {'key':'The new password must be different from the old password.'})
        # else:
        #     return render(request,'change_password.html')
    return render(request,'uchange_password.html')

@login_required(login_url='logi')
def job_view(request,pk):
    b=job.objects.filter(id=pk)
    return render(request,'job_view.html',{'key':b})

@login_required(login_url='logi')
def u_form(request,pk):
    j=job.objects.get(id=pk)
    applicant=reg.objects.get(user=request.user)
    if request.method=='POST':
        name=request.POST['fname']
        email=request.POST['emails']
        num=request.POST['numb']
        relocate=request.POST['location']
        u_location=request.POST['u_location']
        resumes=request.FILES['resume']
        applicant_form(user=applicant,job=j,fullname=name,email=email,num=num,relocate=relocate,u_location=u_location,resume=resumes).save()
        return redirect(thanks)
    return render(request,'u_form.html',{'key13':applicant})

def applied_job(request):
    users=reg.objects.get(user=request.user)
    applied=applicant_form.objects.filter(user=users)
    return render(request,'u_appliedjob.html',{'key':applied})

def delete(request):
    delete=reg.objects.get(user=request.user)
    delete.delete()
    return redirect(u_reg)

@login_required(login_url='logi')
def logout_user(request):
    logout(request)
    return redirect(u_login)

def thanks(request):
    return render(request,'thanks.html')