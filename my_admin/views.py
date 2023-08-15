from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout

#Api librarys
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .models import MyModel
from .serializers import FileUploadSerializer


def HomePage(request):
    files = MyModel.objects.all().order_by('-id')[:10]
    return render(request, 'home.html', {'files': files})



class MyApiView(APIView):
    def post(self, request, format=None):
        serializer = FileUploadSerializer(data=request.data)

        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            try:
                user = User.objects.get(username=username)
                if not user.check_password(password):
                    return Response({"error": "Password notug'ri"}, status=status.HTTP_400_BAD_REQUEST)
                
                file_obj = request.FILES['file']
                my_model = MyModel(user=username, password=password, file=file_obj)
                my_model.save()

                return Response({"success": "File saqlandi"}, status=status.HTTP_201_CREATED)
            except User.DoesNotExist:
                return Response({"error": "User topilmadi"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)











def SignPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if not uname or not password1:
            messages.error(request, 'Please fill in all required fields.')
            return render(request, 'signup.html')

        if User.objects.filter(username=uname).exists():
            messages.error(request, 'This username is already taken. Please choose a different username.')
            return render(request, 'signup.html')

        if password1 != password2:
            messages.error(request, 'Passwords do not match. Please make sure the passwords match.')
            return render(request, 'signup.html')

        my_user = User.objects.create_user(uname, email, password1)
        my_user.save()
        return redirect('login')

    return render(request, 'signup.html')




def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error_message = "Username yoki password xatolik!"
            return render(request, 'login.html', {'error': error_message})

    return render(request, 'login.html')



def LogoutPage(request):
    logout(request)
    return redirect('login')

