from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView

from rest_framework.response import Response

from .models import Movies

from .serializers import MoviesSerializer
# Create your views here.


class MoviesListCreateView(APIView):

    serializer_class = MoviesSerializer

    def get(self,request,*args,**kwargs):

        movies = Movies.objects.all()

        movie_serializer = self.serializer_class(movies,many=True)

        return Response(data= movie_serializer.data ,status=200)


    def post(self, request , *args , **kwargs):

        print(request.data.get('cast'))

        print(request.data)

        movie_serializer = self.serializer_class(data= request.data)

        if movie_serializer.is_valid():

            movie_serializer.save()

            return Response(data={'msg': 'Movie created successfully!!'}, status=200)
        
        return Response (data=movie_serializer.errors,status=400)