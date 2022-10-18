from ast import Delete
from typing import Generic
from urllib import response
from rest_framework import status, views
from rest_framework.response import Response
from rest_framework import generics
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from hospitalhouseapp import serializers
from hospitalhouseapp.models import usuario
from hospitalhouseapp.models.usuario import Usuario
from hospitalhouseapp.serializers import Usuarioserializers, usuarioserializers



class usuarioListView(generics.ListAPIView):
    queryset = Usuario.objects.all()
    serializer_class = Usuarioserializers
    #permission_classes =  (IsAuthenticated,)  

    def list(self,  request):
        print('GET A todos los usuarios ')
        queryset = self.get_queryset()
        serializer = Usuarioserializers(queryset, many= True)
        return Response(serializer.data)


class UsuarioRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = usuarioserializers
    lookup_field = "id"
    lookup_url_kwarg = "pk" 

    def get(self, request, *args, **kwargs):
        print("get a usuario")
        return super().get(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        print("put a usuario")
        return super().put(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        print("delete de usuario")

