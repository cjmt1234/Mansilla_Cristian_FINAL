from django.http import JsonResponse
from django.shortcuts import render
from .serializers import InscritosSerializer, InstitucionSerializer
from .models import Inscritos, Institucion
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from EvaFinalApp.forms import FormInscritos, FormInstitucion

from rest_framework.views import APIView
from django.http import Http404

# Create your views here.

# vista Menú  principal
def index(request):
    return render(request, 'index.html')

# vista Api Autor del programa - Mis datos
def Autor(request):
    emp = {
        'id' : 1,
        'rut':'20280475-6',
        'nombres' : 'Cristian Jose',
        'apellidos': 'Mansilla Troncoso',
        'email' : 'cristian.mansilla13@inacapmail.cl',
    }
    return JsonResponse(emp)



# CLASS BASED VIEWS para las incripciones

class Inscritos_class(APIView):
    def get(self, request):
        inscrit = Inscritos.objects.all()
        serial = InscritosSerializer(inscrit, many=True)
        return Response(serial.data)
    
    def post(self, request):
        serial = InscritosSerializer(data = request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
    
class InscritosDetalle_class(APIView):
        
        def get_object(self, id):
            try:
                return Inscritos.objects.get(pk=id)
            except Inscritos.DoesNotExist:
                return Http404
        
        def get(self, request, id):
            inscrit = self.get_object(id)
            serial = InscritosSerializer(inscrit)
            return Response(serial.data)
        
        def put(self, request, id):
            inscrit = self.get_object(id)
            serial = InscritosSerializer(inscrit, data=request.data)
            if serial.is_valid():
                serial.save()
                return Response(serial.data)
            return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
        
        def delete(self, request, id):
            inscrit = self.get_object(id)
            inscrit.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

   





# FUNCTION BASED VIEWS para la Institución

@api_view(['GET', 'POST'])
def institucion_list(request):
    if request.method == 'GET':
        insti = Institucion.objects.all()
        serial = InstitucionSerializer(insti, many=True)
        return Response(serial.data)
    
    if request.method == 'POST':
        serial = InstitucionSerializer(data = request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.data, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def institucion_detalle(request, id):
   
        try:
            insti = Institucion.objects.get(pk=id)
        except Institucion.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        if request.method == 'GET':
            serial = InstitucionSerializer(insti)
            return Response(serial.data)
            
        if request.method == 'PUT':
            serial = InstitucionSerializer(insti, data=request.data)
            if serial.is_valid():
                serial.save()
                return Response(serial.data)
            return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
        
        if request.method == 'DELETE':
            insti.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
  



    #Vista para agregar Inscritos
def agregarInscrito(request):

   
    if request.method == 'POST':
        form = FormInscritos(request.POST)
        Institu = Institucion.objects.all()

        NomInstitucion = [(nomInst.nombre, nomInst.nombre) for nomInst in Institu]
    # Actualizar las opciones del campo 'estado'
        form.fields['institucion'].widget.choices = NomInstitucion
        if form.is_valid():
           
            form.save()
            return render(request, 'exitoso.html')
    else:
        form = FormInscritos()  
        Institu = Institucion.objects.all()

        NomInstitucion = [(nomInst.nombre, nomInst.nombre) for nomInst in Institu]
    # Actualizar las opciones del campo 'estado'
        form.fields['institucion'].widget.choices = NomInstitucion
    return render(request, 'agregarInscrito.html', {'form':form})


    #Vista para agregar Institución
def agregarInstitucion(request):

    if request.method == 'POST':
        form = FormInstitucion(request.POST)
        if form.is_valid():
           
            form.save()
            return render(request, 'exitoso.html')
    else:
        form = FormInstitucion()  
    return render(request, 'agregarInstitucion.html', {'form':form})