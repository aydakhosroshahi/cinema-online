from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'نام کاربری یا رمز عبور اشتباه است')

    return render(request, 'accounts/login.html')


def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # اعتبارسنجی
        if not username or not email or not password:
            messages.error(request, 'لطفاً تمام فیلدها را پر کنید')
        elif password != confirm_password:
            messages.error(request, 'رمز عبور و تکرار آن مطابقت ندارند')
        elif len(password) < 8:
            messages.error(request, 'رمز عبور باید حداقل ۸ کاراکتر باشد')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'این نام کاربری قبلاً ثبت شده است')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'این ایمیل قبلاً ثبت شده است')
        else:
            # ساخت کاربر جدید
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            user.save()
            messages.success(request, 'ثبت نام با موفقیت انجام شد')
            return redirect('/login')

    return render(request, 'accounts/register.html')