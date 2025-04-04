from django.shortcuts import render
from .models import Medicos
from .serializers import MedicosSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello!</h1>"

def create_app():
   return app

@api_view(['GET'])
def detalhar_medico(request, pk):
    try:
        medico = Medicos.objects.get(pk=pk)
    except Medicos.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = MedicosSerializer(medico)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def listar_medicos(request):
    medicos = Medicos.objects.all()
    serializer = MedicosSerializer(medicos, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def criar_consulta(request):
    serializer = MedicosSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def detalhes_consultas(request, pk):
    try:
        medico = Medicos.objects.get(pk=pk)
    except Medicos.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = MedicosSerializer(medico)
    return Response(serializer.data, status=status.HTTP_200_OK)
