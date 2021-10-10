import os
from django.shortcuts import redirect, render
from django.contrib import messages, auth
from django.contrib.auth import get_user_model
User = get_user_model()
from django.core.paginator import Paginator
from schools.models import Applies, Comment, Schools, Teacher
from .models import User
from pages.models import Subject
from datetime import date, datetime, timedelta
import uuid
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from schools.choices import region_choices, school_type_choices



# Registration
def register(request):
    # Checking if user is authenticated 
    if request.user.is_authenticated:
        if request.user.is_staff:
            return redirect('admin_dashboard')
        else:
            return redirect('user_dashboard')
    else:
        if request.method == 'POST':
            #Get from values
            email = request.POST.get('email')
            password = request.POST.get('password')
            password2 = request.POST.get('password2')

            #Check if passwords are similar
            if password == password2:
                #Username is checked
                if User.objects.filter(email=email).exists():
                    messages.error(request, "That email is already taken!")
                    return redirect('register')
                else:
                    #Looks OK
                    #Generating random token
                    auth_token = str(uuid.uuid4()) 
                    user= User.objects.create_user( password=password, email=email, auth_token=auth_token)
                    user.save()
                    # Send the verifaciton link
                    send_mail_after_registration(email, auth_token)
                    return redirect('token_send')   
            else:
                messages.error(request, 'Passwords do not match!')
                return redirect('register')
        else:
            return render(request, 'accounts/register.html')

# Sending token
def token_send(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            return redirect('admin_dashboard')
        else:
            return redirect('user_dashboard')
    else:
        return render(request, 'accounts/register/token_send.html')

# Send verification link
def send_mail_after_registration(request, email, token):
    if request.user.is_authenticated:
        if request.user.is_staff:
            return redirect('admin_dashboard')
        else:
            return redirect('user_dashboard')
    else:
        subject = 'Your accounts need to be verified'
        message = f'Hi paste the link to verify your account http://127.0.0.1:8000/accounts/verify/{token}'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email]
        send_mail(subject, message , email_from ,recipient_list)

# Verification
def verify(request, auth_token):
    try:
        user_obj = User.objects.filter(auth_token=auth_token).first()
        if user_obj:
            if user_obj.is_verified:
                messages.success(request, 'Your account is already verified.')
                return redirect('login')
            user_obj.is_verified = True
            user_obj.save()
            messages.success(request, 'Your account has been verified.')
            return redirect('login')
        else:
            return redirect('error')
    except Exception as e:
        print(e)
    return redirect('login')

# Error if the token is wrong in the url
def error(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            return redirect('admin_dashboard')
        else:
            return redirect('user_dashboard')
    else:
        return render(request, 'accounts/register/error.html')


#----------------------------------------------------------------------------------------------------------- 
# Login
def login(request):
    # Checking if user is authenticated 
    if request.user.is_authenticated:
        if request.user.is_staff:
            return redirect('admin_dashboard')
        else:
            return redirect('user_dashboard')
    else:
        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']
            # Checking the email exists in database or not
            user_obj = User.objects.filter(email=email).first()
            # Checking user is null or not
            if user_obj is None:
                messages.success(request, 'User not found.')
                return redirect('login')
            # Cheking whether user is verified or not
            if not user_obj.is_verified:
                messages.error(request, 'Profile has not been verified yet. Check your mail')
                return redirect('login')
            # Looks good
            user = auth.authenticate(email=email, password=password)

            if user is not None:
                auth.login(request,user)
                messages.success(request, 'You are logged in!')
                # Ckecking whether admin or user dashboard login
                if user.is_staff == True:
                    return redirect('admin_dashboard')
                else:
                    return redirect('user_dashboard')
            else:
                messages.error(request,'Invalid ceradentials!')
                return render(request, 'accounts/login.html')
        else:
            return render(request, 'accounts/login.html')

#-----------------------------------------------------------------------------------------------------------
# Reset password 
# Sending email with token
def reset_pass_send_email(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            return redirect('admin_dashboard')
        else:
            return redirect('user_dashboard')
    else:
        if request.method =='POST':
            email = request.POST.get('reset_password')
            user_obj = User.objects.filter(email=email).first()
            # Checking if user is not null
            if user_obj is not None:
                # Cheking if user is verified or not
                if (user_obj.is_verified):
                    get_token = user_obj.auth_token
                    send_mail_reset_password(email, get_token)
                    return redirect('token_send')
                else:
                    messages.success(request, 'Enter the verified email.')
                    return redirect('reset_pass_send_email')
            elif user_obj is None:
                messages.success(request, 'Enter the registered email.')
                return redirect('reset_pass_send_email')
        return render(request, 'accounts/register/reset_pass_send_email.html')

# Returning reset password form 
def reset_password(request, get_token):
    context = {
        'get_token':get_token
    }
    return render(request, 'accounts/register/reset_password_form.html', context)

# Sending mail
def send_mail_reset_password(email , get_token):
    subject = 'Reset Password'
    message = f'Follow this link to reset your password http://127.0.0.1:8000/accounts/reset_password/{get_token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message , email_from ,recipient_list)
    
# Changing password if they are match
def reset_password_form(request, get_token):
    try:
        if request.method =='POST':
            password = request.POST['pass1']
            password2 = request.POST['pass2'] 
    
            user_obj = User.objects.filter(auth_token = get_token).first()

            if (password == password2):
                if user_obj:
                    user_obj.set_password(password)
                    user_obj.save()
                    return redirect('login')
            else:
                messages.success(request, 'Passwords are not matching.')
                return redirect('reset_password',get_token)
        context = {
            'get_token':get_token
        }

        return render(request,'accounts/register/reset_password_form', context)

    except Exception as e:
        print(e)


#----------------------------------------------------------------------------------------------------------- 
# Admin Dashboard
@login_required(login_url='/accounts/login')
def admin_dashboard(request): 
    # Count how many comments 
    comments = Comment.objects.count()
    # Count how many users
    user_obj = User.objects.count()
    # Count how many users
    school_num = Schools.objects.count()
    # Count how many applies
    all_applies = Applies.objects.count()

    todaycomments = Comment.objects.all().extra({'date_created' : "date(created_at)" }).values('date_created').count()
    todayapplies = Applies.objects.all().extra({'date_created': "date(created_at"}).values('date_created').count()
    todayusers = User.objects.all().extra({'date_created': "date(created_at"}).values('date_created').count()

    context = {
        'comments':comments,
        'tadaycomments': todaycomments,
        'todayapplies': todayapplies,
        'all_applies': all_applies,
        'todayusers':todayusers,
        'school_num': school_num
    }
    return render(request, 'accounts/admin/admin_dashboard.html', context)


#----------------------------------------------------------------------------------------------------------- 
# User Dashboard 
@login_required(login_url='/accounts/login')
def user_dashboard(request): 
    return render(request, 'accounts/user_dashboard.html')


#----------------------------------------------------------------------------------------------------------- 
# Profile settings 
@login_required(login_url='/accounts/login')
def profile(request):
    user = User.objects.get(id=request.user.id)
    #Cheking whether admin or user profile settings and it match appropriate template
    if request.user.is_staff:
        is_staff = True
    else:
        is_staff = False

    context = {
        'is_staff':is_staff,
        'user': user
    }

    return render(request, 'accounts/profile.html', context)

# Update Profile settings
@login_required(login_url='/accounts/login')
def profile_save(request, user_id):
    if request.method == 'POST':
        f_name = request.POST.get('first_name')
        l_name = request.POST.get('last_name')
        p_photo = request.FILES.get('profile_photo')
        # Match correspond user
        user = User.objects.get(id=user_id)
        # check photo is not null, and name assigned to photo name
        if p_photo is not None:
            fs = FileSystemStorage()
            name = fs.save(p_photo.name, p_photo)        
        if user is not None:
            user.first_name = f_name
            user.last_name = l_name
            if p_photo is not None:
                # Delete image old image path if old image
                if len(str(user.profile_photo))>0:
                    os.remove(user.profile_photo.path)
                user.profile_photo = name
            user.save()
            return redirect('profile')
    else:
        return redirect('profile_admin')

# Delete Profile image
@login_required(login_url='/accounts/login')
def profile_photo_delete(request, profile_id):
    if request.method == "POST":
        user = User.objects.get(id=profile_id)
        if len(str(user.profile_photo))>0:
            os.remove(user.profile_photo.path)
        user.profile_photo.delete()
    return redirect('profile')

#----------------------------------------------------------------------------------------------------------- 
# Account delete 
@login_required(login_url='/accounts/login')
def account_delete(request, id):
    if request.method == 'POST':
        user = User.objects.get(id=id)
        if user is not None:
            # delete image path also from media folder
            os.remove(user.profile_photo.path)
            user.delete()
            return redirect('register')
        else:
            messages.error('User not found')
            return redirect('profile')
    else:
        return redirect('profile')

#----------------------------------------------------------------------------------------------------------- 
# Schools section 
@login_required(login_url='/accounts/login')
def schools(request):
    schools = Schools.objects.all().order_by('-id')
    # Pagination schools
    paginator = Paginator(schools,5)
    page = request.GET.get('page')
    paged_schools = paginator.get_page(page)
    
    if request.user.is_staff:
        is_staff = True
    else:
        is_staff = False
    
    context = {
        'is_staff':is_staff,
        'schools': paged_schools
    }

    return render(request, 'accounts/schools.html',context)


#----------------------------------------------------------------------------------------------------------- 
# Teachers section 
@login_required(login_url='/accounts/login')
def teachers(request):
    teachers = Teacher.objects.all().order_by('-ranking')

    if request.user.is_staff:
        is_staff = True
    else:
        is_staff = False

    context = {
        'is_staff':is_staff,
        'teachers': teachers
    }

    return render(request, 'accounts/teachers.html',context)


#----------------------------------------------------------------------------------------------------------- 
# Subject section
@login_required(login_url='/accounts/login')
def subjects(request):
    subjects = Subject.objects.all().order_by('-id')
    
    context = {
        'subjects': subjects
    }

    return render(request, 'accounts/admin/subjects.html',context)


#----------------------------------------------------------------------------------------------------------- 
# Comments Section
@login_required(login_url='/accounts/login')
def comments(request, id):
    user = User.objects.get(id=request.user.id)
    # Get comments all if admin or get comments to belonged particular user
    if user.is_staff == True:
        comments = Comment.objects.all().order_by('-created_at')
    else: 
        comments = Comment.objects.filter(user_id=request.user.id)
    
    today = date.today()
    enddate = datetime.today()
    startdate = enddate - timedelta(days=6)
    # Filtering by date all/today/yesterday/week/month 
    if id==0:
        comments = comments.all().order_by('id')
    if id==1:
        comments = comments.filter(created_at__day = today.day, created_at__month=today.month, created_at__year=today.year).order_by('id')
    if id ==2:
        comments = comments.filter(created_at__day = today.day-1, created_at__month=today.month, created_at__year=today.year).order_by('id')
    if id ==3:
        comments = comments.filter(created_at__range=[startdate, enddate]).order_by('id')
    if id ==4:
        comments = comments.filter(created_at__month=today.month, created_at__year=today.year,).order_by('id')
    
    if request.user.is_staff:
        is_staff = True
    else:
        is_staff = False
    # Pagination
    paginator = Paginator(comments,5)
    page = request.GET.get('page')
    paged_comments = paginator.get_page(page)

    context = {
        'is_staff':is_staff,
        'comments': paged_comments
    }

    return render(request, 'accounts/comments.html',context)

# Comments Delete 
@login_required(login_url='/accounts/login')
def comments_delete(request, id):
    comment = Comment.objects.get(id=id) 
    comment.delete()
    messages.success(request, "Comment with id: "+str(id)+' is deleted' )
    return redirect('comments', 0)

# Hide or Unhide comments 
@login_required(login_url='/accounts/login')
def comments_hide_unhide(request, id):
    comment = Comment.objects.get(id=id) 
    # if hidden => unhide, or make hidden
    if comment.hidden == True:
        comment.hidden = False
    elif comment.hidden == False:
        comment.hidden =True

    comment.save()
    messages.success(request, "Comment with id: "+str(id)+' is hidden from now' )
    
    return redirect('comments', 0)


#----------------------------------------------------------------------------------------------------------- 
# Apply section 
@login_required(login_url='/accounts/login')
def applies(request,apply_type):
    user = User.objects.get(id=request.user.id)
    # Get all applies if admin, or get appropriate applies
    if user.is_staff == True:
        applies = Applies.objects.all().order_by('-created_at')
    else: 
        applies = Applies.objects.filter(user_id=request.user.id)
    
    # Filter by all/on_process/received/rejected
    if (apply_type =='all'):
        applies = applies.all().order_by('-created_at')
    if(apply_type == 'process'):
        applies = applies.filter(status=2)
    if(apply_type=='received'):
        applies = applies.filter(status=1)
    if(apply_type=='rejected'):
        applies = applies.filter(status=0)
    
    # Pagination
    paginator = Paginator(applies,5)
    page = request.GET.get('page')
    paged_applies = paginator.get_page(page)
    
    if request.user.is_staff:
        is_staff = True
    else:
        is_staff = False

    context = {
        'is_staff':is_staff,
        'applies': paged_applies
    }
    
    return render(request, 'accounts/applies.html',context)

# Making Apply 
@login_required(login_url='/accounts/login')
def making_apply(request,id ):
    if request.method == 'POST':
        f_name = request.user.first_name
        l_name = request.user.last_name
        email = request.user.email
        region = request.POST.get('region')
        school_name = request.POST.get('school_name')
        body = request.POST.get('body')
        apply = Applies.objects.create(first_name=f_name, last_name=l_name, email=email, region=region, school="Umid",body=body,user_id=id, status=2)
        
        if apply is not None:
            apply.save()
            return redirect('applies' , id)
    context ={
        'region_choices':region_choices,
        'school_type_choices':school_type_choices,
    }

    return render(request, 'accounts/making_apply.html', context)


# Receive apply by admin 
@login_required(login_url='/accounts/login')
def receive_apply(request, id):
    apply = Applies.objects.get(id=id) 
    apply.status = 1 
    #  1 means received
    # Received time
    apply.received_at = datetime.now()
    apply.save()
    messages.success(request, "Apply with id: "+str(id)+' is recieved' )
    
    return redirect('applies', 'all')

# Reject Apply 
@login_required(login_url='/accounts/login')
def reject_apply(request, id):
    apply = Applies.objects.get(id=id) 
    apply.status = 0
    # 0 means rejected
    # Rejected time
    apply.rejected_at = datetime.now()
    apply.save()
    messages.success(request, "Apply with id: "+str(id)+' is rejected' )

    return redirect('applies', 'all')


# Full info about apply with particular id 
@login_required(login_url='/accounts/login')   
def apply_full_info(request,id):
    apply = Applies.objects.get(id=id)
    
    context ={
        'apply':apply
    }

    return render(request,'accounts/admin/apply_full_info.html',context)


# Apply_delete 
@login_required(login_url='/accounts/login')   
def apply_delete(request, id):
    apply = Applies.objects.get(id=id) 
    apply.delete()
    messages.success(request, "Apply with id: "+str(id)+'is deleted' )
    return redirect('applies', 'all')


#----------------------------------------------------------------------------------------------------------- 
# Logout
@login_required(login_url='/accounts/login')
def logout(request):
    auth.logout(request)
    return redirect('index')


