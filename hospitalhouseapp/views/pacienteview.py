from rest_framework import generics, status
from rest_framework.response  import Response
#from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from hospitalhouseapp.serializers.pacienteserialiserz import Pacienteserializers
from hospitalhouseapp.serializers.usuarioserializers import Usuarioserializers
from hospitalhouseapp.models.paciente  import Paciente

class PacienteListCreateView(generics.ListCreateAPIView):
    queryset = Paciente.objects.all()
    serializer_class = Pacienteserializers
    #permission_classes =  (IsAuthenticated,)  

    def list(self,  request):
        print('GET A todos los Medicos ')
        queryset = self.get_queryset()
        serializer = Pacienteserializers(queryset, many= True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        print("post de paciente ")
        print(request.data)
        usuarioData = request.data.pop('usuario')
        serializerU = Usuarioserializers(data=usuarioData)
        serializerU.is_valid(raise_exception=True)
        usuario = serializerU.save()
        enfData = request.data
        enfData.update({"usuario":usuario.id})
        serializerEnf = Pacienteserializers(Data=enfData)
        serializerEnf.is_valid(raise_exception=True)
        serializerEnf.save()
        return Response(status=status.HTTP_201_CREATED)


class PacienteRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
        queryset = Paciente.objects.all()
        serializer_class = Pacienteserializers
        lookup_field = "id"
        lookup_url_kwarg = "pk" 

        def get(self, request, *args, **kwargs):
            print("get a paciente ")
            """token = request.META.get('HTTP_AUTHORIZATION')[7:]
            tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
            valid_data = tokenBackend.decode(token,verify=False)

            if valid_data['user_id'] != kwargs['pk']:
                stringResponse = {'detail':'Unauthorized Request'}
                return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)"""
            return super().get(request, *args, **kwargs)
    
        def put(self, request, *args, **kwargs):
            print("put a Medico")
            return super().put(request, *args, **kwargs)

        def delete(self, request, *args, **kwargs):
            print("delete de Medico")
            return super().delete(request, *args, **kwargs)