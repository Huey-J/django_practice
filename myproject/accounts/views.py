from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
    if request.method == 'POST':    # POST방식으로 요청되면
        if request.POST['password1'] == request.POST['password2']:  # 입력된 pw 2개 같은지 확인
            # 회원정보 추가
            user = User.objects.create_user(
                username=request.POST['account'], password=request.POST['password1']
            )
            # 로그인 처리
            auth.login(request, user)
            # blog 페이지로 redirect
            return redirect('home')
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['account']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password) # 회원정보 찾기

        if user is not None:    # 정보 있으면 로그인 처리
            auth.login(request, user)
            return redirect('home')
        else:   # 정보 없으면 에러 띄우고 로그인페이지 redirect
            return render(request, 'login.html', {'error': 'incorrect'})
    else:
        return render(request, 'login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    return render(request, 'login.html')
