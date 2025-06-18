from django.shortcuts import render


from rest_framework.views import APIView

from django.contrib.auth import authenticate

from rest_framework.response import Response

from rest_framework_simplejwt.tokens import RefreshToken

from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework.permissions import AllowAny

from .serializers import ProfileSerializer

from .models import OTP

from django.db import transaction

from .utility import sending_sms

class LoginView(APIView):

    http_method_names =['post']


    def post(self, request, *args,**kwargs):

        username = request.data.get('username')

        password = request.data.get('password')

        user = authenticate(username=username,password=password)

        if user:

            # if user then create token

            access_token = RefreshToken.for_user(user).access_token

            # then we have to pass 

            return Response(data={'access_token' : str(access_token)},status=200)
        
        return Response(data={'msg': 'invalid credentials'}, status=401)


class UserRegistrationView(APIView):


    http_method_names = ['post']

    authentication_classes = [JWTAuthentication]

    permission_classes = [AllowAny]

    serializer_class = ProfileSerializer

    def post(self , request , *args , **kwargs):

        serializer = self.serializer_class(data= request.data)

        if serializer.is_valid():

            with transaction.atomic():

                profile= serializer.save()

                profile.role = 'User'

                email = request.data.get('email')

                password = request.data.get('password')

                profile.set_password(password)

                profile.username = email

                profile.save()

                otp = '1254'

                otp_obj = OTP.objects.create(user = profile , otp=otp)

                phone_num = f'+91{profile.mobile_num}'

                sending_sms(phone_num,otp)


                return Response(data= {'msg' : 'verify account using otp'}, status=200)
        
        return Response(data=serializer.errors, status=400)

             


